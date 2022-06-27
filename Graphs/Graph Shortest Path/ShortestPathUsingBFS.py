# Finding shortest path from source to destination(Single source) using BFS.

from collections import defaultdict, deque


class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.adjList = defaultdict(list)
    
    def add_edge(self, v1, v2):
        self.adjList[v1].append(v2)
        self.adjList[v2].append(v1)
    

def shortest_path(graph, source, destination):
    parent = [-1] * (graph.V+1)
    queue = deque()
    visited = [False] * (graph.V+1)
    visited[source] = True
    queue.append(source)
    while queue:
        node = queue.popleft()
        for neig in graph.adjList[node]:
            if not visited[neig]:
                visited[neig] = True
                parent[neig] = node
                queue.append(neig)
    #print(parent)
    shortest_path = []
    curr = destination
    while curr != source:
        shortest_path.append(curr)
        curr = parent[curr]
    
    shortest_path.append(source)
    print(shortest_path[::-1])

g = Graph(8)
g.add_edge(1,2)
g.add_edge(1,3)
g.add_edge(1,4)
g.add_edge(2,5)
g.add_edge(3,8)
g.add_edge(4,6)
g.add_edge(5,8)
g.add_edge(6,7)
g.add_edge(7,8)
shortest_path(g,1,8)
