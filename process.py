# pip install Dijkstar
import os
from dijkstar import Graph, find_path, NoPathError

# Read graph file
graph = Graph()
nodes = []

with open("graph.txt", 'r') as f:
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

# verify
print(graph)
try:
    print(find_path(graph, 1,8))
except NoPathError:
    print("No path found!")

# Calculate degree for each node
# For each node, go through all the graph and for each link, add 1
# print("Degrees:")
# for node in nodes:
#     if node in graph:
#         degree = len(graph[node])/2
#         print(f'Node {node}: {degree}')
#     else:
#         print(f'Node {node}: 0')

# Calculate betweenness for each node


# Calculate closeness for each node
print("Closeness:")
for i in nodes:

    shortestPathSum = 0
    for j in nodes:
        if i == j:
            continue

        cost = 0
        try:
            cost = find_path(graph, i, j).total_cost
        except NoPathError:
            cost = 0

        shortestPathSum = shortestPathSum + cost

    closeness = (len(nodes)-1) / shortestPathSum
    print(f'Node {i}: {closeness}')



# Calculate Clustering Coefficient for each node

