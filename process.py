import os

# Read graph file
graph = []
nodes = []
with open("graph.txt", 'r') as f:
    for line in f.readlines():
        strList = line.split(' ')
        arr = []
        for s in strList:
            node = int(s)
            arr.append(node)
            if node not in nodes:
                nodes.append(node)
        graph.append(arr)

# verify
print(graph)
print(nodes)

# Calculate degree for each node

# Calculate betweenness for each node


# Calculate closeness for each node


# Calculate Clustering Coefficient for each node

