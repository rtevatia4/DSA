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

from collections import defaultdict


class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.adjList = defaultdict(list)

    def add_edge(self, v1, v2):
        self.adjList[v1].append(v2)
        self.adjList[v2].append(v1)

def dfs(vertex, count):
    global maxCount, node
    visited.add(vertex)
    count+=1
    for neigh in g.adjList[vertex]:
        if neigh not in visited:
            if count > maxCount:
                maxCount = count
                node = neigh
            dfs(neigh, count)
    

if __name__ == "__main__":
    f = open("C:\RahulTevatia\DSA\Graphs\Questions\graph.txt", "r")
    vertices = int(f.readline())
    g = Graph(vertices)
    for line in f:
        v1, v2 = line.split()
        g.add_edge(int(v1),int(v2))
    f.close()
    print(g.adjList)
    visited = set()
    path = 0
    maxCount = -10**31
    node = 0
    
    for vertex in g.adjList:
        if vertex not in visited:
            dfs(vertex, path)
    print(maxCount, node)

    path = 0
    maxCount = -10**31
    visited = set()
    dfs(node, path)
    print(maxCount, node)