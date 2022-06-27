"""
Kahn's Algorithm is based on BFS. It maintains the in degree. And based on the theorem:
That in a DAG there must be atleast one vertex with in_degree = 0 and one vertex with out_degree=0

Implemented finding topological ordering and detecting cycle
"""
from collections import defaultdict
import collections


class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.adjList = defaultdict(list)
    
    def add_edge(self, v1, v2):
        self.adjList[v1].append(v2)
    
    def topological_sort(self):
        in_degree = [0] * (self.V)
        for vertex, edges in self.adjList.items():
            for edge in edges:
                in_degree[edge] += 1
        #print(in_degree)
        queue = collections.deque()
        for vertex, degree in enumerate(in_degree):
            if degree == 0:
                queue.append(vertex)
        
        result = []
        cycle = 0
        while queue:
            node = queue.popleft()
            result.append(node)
            for nei in self.adjList[node]:
                in_degree[nei] -= 1
                if in_degree[nei] == 0:
                    queue.append(nei)
            cycle += 1
        if cycle != self.V:
            print("cycle in graph")
        else:
            print(result)

"""
Sample graph
             7<-- ---> 6
                 |     ^
                 |     |
0->  1 --> 2 --> 4 --> 5
     |           ^
     |           |
     |---------->3          
"""
g = Graph(8)
g.add_edge(0,1)
g.add_edge(1,2)
g.add_edge(1,3)
g.add_edge(2,4)
g.add_edge(3,4)
g.add_edge(4,5)
g.add_edge(4,6)
g.add_edge(4,7)
g.add_edge(5,6)
g.topological_sort()
