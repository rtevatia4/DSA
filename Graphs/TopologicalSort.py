# Finding the topological ordering using DFS
from collections import defaultdict


class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.adjList = defaultdict(list)
    
    def add_edge(self, v1, v2):
        self.adjList[v1].append(v2)
    
    def topological_sort_util(self, node, stack, visited):
        visited.add(node)
        for nei in self.adjList[node]:
            if nei not in visited:
                self.topological_sort_util(nei, stack, visited)
        stack.append(node)

    def topological_sort(self):
        """
        Class method to find the topological ordering using DFS based approach
        """
        stack = []
        visited = set()
        for node in range(1, self.V+1):
            if node not in visited:
                self.topological_sort_util(node, stack, visited)

        print("Topological Ordering")
        while len(stack) > 0:
            print(stack.pop(), end=" ")

"""
Sample graph
             7<-- ---> 6
                 |     ^
                 |     |
     1 --> 2 --> 4 --> 5
     |           ^
     |           |
     |---------->3          
"""
g = Graph(7)
g.add_edge(1,2)
g.add_edge(1,3)
g.add_edge(2,4)
g.add_edge(3,4)
g.add_edge(4,5)
g.add_edge(4,6)
g.add_edge(4,7)
g.add_edge(5,6)
g.topological_sort()