# pip install Dijkstar
import os
from dijkstar import Graph
from decimal import Decimal


# Read graph file
graph = Graph()
nodes = []

with open("graph_test.txt", 'r') as f:
    for line in f.readlines():
        strList = line.split(' ')

        # Edge has to be added both ways since the data structure doesn't support undirected graphs
        graph.add_edge(int(strList[0]), int(strList[1]), 1)
        graph.add_edge(int(strList[1]), int(strList[0]), 1)

        # Create a node list
        if int(strList[0]) not in nodes:
            nodes.append(int(strList[0]))
        if int(strList[1]) not in nodes:
            nodes.append(int(strList[1]))

community_list = []


# Different Attempt ---------------------------------------------------
new_community_list = []
density_list = []

for node in nodes:
    if node in graph:
        new_community1 = []
        new_community1.append(node)
        neighbors = graph[node]
        degree = len(neighbors)

        if degree > 1:
            #Find neighbors of current neighbor of current node
            for node1 in neighbors:
                neighborsNext = graph.get(node1, [])
                if node1 not in new_community1:
                    new_community1.append(node1)
                density = CalculateDensity(graph, new_community1)
                
                #Check if first neighbor has similar neighbor as current node
                for node2 in neighborsNext:
                    if node2 in neighbors:
                        if node2 not in new_community1:
                            new_community1.append(node2)
                        
                        density = CalculateDensity(graph, new_community1)
                        if density < 0.7:
                            new_community1.remove(node2)
                            density = CalculateDensity(graph, new_community1)
                            break

        new_community1.sort()
        density_decimal = Decimal(density).quantize(Decimal("1.000"))
        density_string = 'Density: ' + str(density_decimal)
        new_community1.append(density_string)
        
        if new_community1 not in new_community_list:
            if density >= 0.7:
                if len(new_community1) > 2:
                    new_community_list.append(new_community1)


print("Different Method")
print(new_community_list)
print("\n ----------------- \n")
# End Different Attempt -----------------------------------------------------



# Our Original Attempt
def FindHighestDegreeNode (graph):
    highest_degree_node = None

    for node in nodes:
        if node in graph:
            degree = len(graph[node])

            if highest_degree_node is None:
                highest_degree_node = node
            elif degree > len(graph[highest_degree_node]):
                highest_degree_node = node

    return highest_degree_node


def overlap (a1, a2):
    count = 0
    for i in a1:
        if i in a2:
            count = count + 1
    return count


def FindHighestDegreeNeighbor(graph, community):
    highest_overlap_neighbor = None
    highest_overlap = None

    for node in community:
        for neighbor in graph[node]:
            if neighbor in community:
                continue

            o = overlap(community, graph[neighbor])
            if highest_overlap is None:
                highest_overlap_neighbor = neighbor
                highest_overlap = o
            elif o > highest_overlap:
                highest_overlap_neighbor = neighbor
                highest_overlap = o
            elif o == highest_overlap:
                if len(graph[neighbor]) > len(graph[highest_overlap_neighbor]):
                    highest_overlap_neighbor = neighbor
                    highest_overlap = o


    return highest_overlap_neighbor


# The `CalculateDensity` function takes a graph object and a list of nodes representing a community and calculates the density of that community.
def CalculateDensity(graph, new_community):
    number_of_nodes = len(new_community)   # Get the number of nodes in the new community

    edges = 0.0
    for node in new_community:
        for neighbor in graph[node]:
            if neighbor in new_community:
                edges = edges + 1

    density = edges / (number_of_nodes * (number_of_nodes - 1))

    return density


def updateGraph(graph, community):
    # Remove all nodes  (with their edges) that are not linked to any other nodes outside new_community
    for node in community:
        remove_flag = True
        for neighbor in graph[node]:
            if neighbor not in community:
                remove_flag = False
                break

        if remove_flag:
            graph.remove_node(node)

    return graph


while graph.node_count > 2:
    new_community = []

    # Find node with highest degree
    node = FindHighestDegreeNode(graph)
    next_node = node

    new_community.append(node)

    density = 1
    while True:
        # Find the neighbor with the highest degree
        next_node = FindHighestDegreeNeighbor(graph, new_community)
        if next_node is None:
            break
        new_community.append(next_node)

        # print(new_community)
        density = CalculateDensity(graph, new_community)
        # print(density)

        if density < 0.7:
            new_community.remove(next_node)
            break
        node = next_node

    density = CalculateDensity(graph, new_community)
    graph = updateGraph(graph, new_community)
    new_community.sort()
    density_decimal = Decimal(density).quantize(Decimal("1.000"))
    density_string = 'Density: ' + str(density_decimal)
    new_community.append(density_string)
    community_list.append(new_community)

print("Our Original Method")
print(community_list)



# Combine Results of Both Attempts
all_communities = []
for i in community_list:
    if i not in new_community_list:
        new_community_list.append(i)

all_communities.append(new_community_list)

print("\n ----------------- \n")
print("Combined Lists")
print(all_communities)
