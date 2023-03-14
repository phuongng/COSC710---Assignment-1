# pip install Dijkstar
import os
from dijkstar import Graph, find_path

# Read graph file
graphList = []
graph = Graph()
nodes = []

with open("graph.txt", 'r') as f:
    for line in f.readlines():
        strList = line.split(' ')
        graph.add_edge(int(strList[0]), int(strList[1]), 1)

# verify
print(graph)
print(find_path(graph, 1,7))

# Calculate degree for each node
# For each node, go through all the graph and for each link, add 1


# Calculate betweenness for each node


# Calculate closeness for each node


# Calculate Clustering Coefficient for each node

