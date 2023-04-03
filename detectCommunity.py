# pip install Dijkstar
import os
from dijkstar import Graph

#Methods
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


def FindHighestDegreeNeighbor (graph, node):
    highest_degree_neighbor = None
    
    for neighbor in graph[node]:
        if neighbor in graph:
            degree = len(graph[neighbor])

            if highest_degree_neighbor is None:
                highest_degree_neighbor = neighbor
            elif degree > len(graph[highest_degree_neighbor]):
                highest_degree_neighbor = neighbor

    return highest_degree_neighbor


def CalculateDensity(graph, new_community):
    return .6

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

# Read graph file
graph = Graph()
nodes = []

with open("karate.txt", 'r') as f:
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

while graph.node_count > 0:
    new_community = []

    # Find node with highest degree
    node = FindHighestDegreeNode(graph)

    new_community.append(node)

    density = 1
    while density >= 0.7:
        # Find the neighbor with the highest degree
        next_node = FindHighestDegreeNeighbor(graph, node)
        new_community.append(next_node)

        density = CalculateDensity(graph, new_community)
        node = next_node

    graph = updateGraph(graph, new_community)
    community_list.append(new_community)
