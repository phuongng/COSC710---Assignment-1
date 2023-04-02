# pip install Dijkstar
import os
from dijkstar import Graph

#Methods
def FindHighestDegreeNode (graph):
    return "x"

def FindHighestDegreeNeighbor (graph, node):
    return "x"

def CalculateDensity(graph, new_community):
    return .6

def updateGraph(graph, community):
    # Remove all nodes  (with their edges) that are not linked to any other nodes outside new_community
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

    updateGraph(graph, new_community)
    community_list.append(new_community)
