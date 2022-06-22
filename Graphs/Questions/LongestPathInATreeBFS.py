"""You are given an unweighted, undirected tree. 
Write a program to output the length of the longest path (from one node to another) in that tree.
 The length of a path in this case is number of edges we traverse from source to destination.

Input
The first line of the input file contains one integer N --- number of nodes in the tree (0 < N <= 10000). 
Next N-1 lines contain N-1 edges of that tree --- Each line contains a pair (u, v) means there is an edge between 
node u and node v (1 <= u, v <= N).

Output
Print the length of the longest path on one line.

Example
Input:
3
1 2
2 3

Output:
2
"""

from collections import defaultdict, deque

class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.adjList = defaultdict(list)

    def add_edge(self, v1, v2):
        self.adjList[v1].append(v2)
        self.adjList[v2].append(v1)

def bfs(vertex):
    visited = set()
    distance = [-1] * (g.vertices+1)
    distance[vertex] = 0
    visited.add(vertex)
    queue = deque()
    queue.append(vertex)
    while queue:
        front = queue.popleft()
        for neighbor in g.adjList[front]:
            if neighbor not in visited:
                visited.add(neighbor)
                distance[neighbor] = distance[front] + 1
                queue.append(neighbor)
    print(distance)
    maxDis = 0
    for i in range(g.vertices+1):
        if distance[i] > maxDis:
            maxDis = distance[i]
            node = i
    return node, maxDis
    

if __name__ == "__main__":
    f = open("C:\RahulTevatia\DSA\Graphs\Questions\graph.txt", "r")
    vertices = int(f.readline())
    g = Graph(vertices)
    for line in f:
        v1, v2 = line.split()
        g.add_edge(int(v1),int(v2))
    f.close()
    print(g.adjList)
    
    node, dis = bfs(1)
    #print(node, dis)

    node_2, longest_path = bfs(node)
    print("Longest Path is from node %d and node %d with length %d:" %(node, node_2, longest_path))