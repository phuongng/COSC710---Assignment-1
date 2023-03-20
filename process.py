# pip install Dijkstar
import os
from dijkstar import Graph, find_path, NoPathError

# Read graph file
graph = Graph()
nodes = []

with open("graph_test1.txt", 'r') as f:
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
print("Graph:")
print(graph)
print("===========================================================================\n")

# Calculate degree for each node
print("Degrees:")
for node in nodes:
    if node in graph:
        degree = len(graph[node])
        print(f'Node {node}: {degree}')
    else:
        print(f'Node {node}: 0')

# Calculate betweenness for each node
print("===========================================================================\n")
print("Betweenness:")
visited = dict.fromkeys(nodes, 0)
paths = []
global_vars = dict.fromkeys(["min_length"], 1000000000)
def dfs(current, end, between_node, len, isBetween):

    if visited[current]:
        return

    if current == end:
        paths.append([isBetween, len])
        visited[current] = 0
        if len < global_vars["min_length"]:
            global_vars["min_length"] = len
        return

    # Optimization not to go through any path in case a shorter one was already found
    if len + 1 > global_vars["min_length"]:
        return

    if current == between_node:
        global_vars["isBetween"] = 1

    visited[current] = 1

    for node in graph[current]:
        if current == between_node or isBetween == 1:
            flag = 1
        else:
            flag = 0
        dfs(node, end, between_node, len+1, flag)

    visited[current] = 0

def initDfs(paths, visited, global_vars):
    paths.clear()
    visited = dict.fromkeys(nodes, 0)
    global_vars["min_length"] = 1000000000

for node in nodes:

    betweeness = 0.0
    for i in nodes:
        if i == node:
            continue
        for j in nodes:
            if j == node or i == j or i > j:
                continue

            # print (f'{i} - {j} - {node}')
            dfs(i,j, node, 0, 0)

            shortest_count = 0
            between_count = 0
            for path in paths:

                if path[1] == global_vars["min_length"]:
                    shortest_count = shortest_count + 1

                    if path[0] == 1:
                        between_count = between_count + 1

            betweeness = betweeness + (float(between_count)/float(shortest_count))

            # print(f'{i}, {j}, min_len: {global_vars["min_length"]} betweeness: {between_count}/{shortest_count}')
            # print(paths)
            # print(betweeness)
            initDfs(paths, visited, global_vars)

    print(f'Node {node}: {betweeness}')


# Calculate closeness for each node
print("===========================================================================\n")
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
    
print("===========================================================================\n")

# Calculate Clustering Coefficient for each node:  (2 * Number of Neighbor Connections)/(Degree * (Degree-1))
print("Clustering Coefficient:")
for node in nodes:
    if node in graph:
        neighbors = graph[node]
        neighborConnections = 0
        degree = len(neighbors)
        # print(f'Node {node}: {neighbors}')

        if degree > 1:
            #Find neighbors of current neighbor of current node
            for node1 in neighbors:
                neighborsNext = graph.get(node1, [])
                
                #Check if first neighbor has similar neighbor as current node
                for node2 in neighborsNext:
                    if node2 in neighbors:
                        # print(node1, node2)
                        neighborConnections += 1
                        # print(f'Node {node}: {neighborConnections}')
                        
            # Don't need to multiply neighbor connections by 2 since we transformed to a directed graph
            clusterCoeff = (neighborConnections) / (degree * (degree - 1))
            print(f'Node {node}: {clusterCoeff}')
    else:
        print(f'Node {node}: 0')
print("===========================================================================\n")

class SortList:  
    #Represent the head and tail of the singly linked list  
    def __init__(self):  
        self.head = None;  
        self.tail = None;  
                         
    #sortList() will sort nodes of the list in ascending order  
    def sortList(self):  
        #Node current will point to head  
        current = self.head;  
        index = None;  
          
        if(self.head == None):  
            return;  
        else:  
            while(current != None):  
                
    #Node index will point to node next to current  
                index = current.next;  
                  
                while(index != None):  
                    #If current node's data is greater than index's node data, swap the data between them  
                    if(current.data > index.data):  
                        temp = current.data;  
                        current.data = index.data;  
                        index.data = temp;  
                    index = index.next;  
                current = current.next;  
                  
    #display() will display all the nodes present in the list  
    def display(self):  
        #Node current will point to head  
        current = self.head;  
        if(self.head == None):  
            print("List is empty");  
            return;  
        while(current != None):  
            #Prints each node by incrementing pointer  
            print(current.data),  
            current = current.next;  
        print ""  
        betweeness = SortList();  
        closeness = SortList();  
        clusterCoeff = SortList();  
        
        #Sorting list  
betweeness.sortList();  
closeness.sortList();  
clusterCoeff.sortList();  
   
#Displaying sorted list  
print("Sorted betweeness's list: ");  
betweeness.display();  

print("Sorted closeness's list: ");  
closeness.display();  

print("Sorted Clustering Coefficient's list: ");  
clusterCoeff.display();  
