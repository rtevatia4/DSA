"""
Single Source Shortest Path Algorithm.
Here we will be finding the Shortest Path from Single Source using Topological Ordering in O(V+E) time.
Here we can have the negative weights too.
"""
from collections import defaultdict

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.adjList = defaultdict(list)
    
    def add_edge(self, v1, v2, w):
        self.adjList[v1].append((v2,w))
    
    def topological_sort_util(self, node, stack, visited):
        visited.add(node)
        for nei, weight in self.adjList[node]:
            if nei not in visited:
                self.topological_sort_util(nei, stack, visited)
        stack.append(node)

    def topological_sort(self):
        """
        Class method to find the topological ordering using DFS based approach
        """
        stack = []
        visited = set()
        for node in range(self.V):
            if node not in visited:
                self.topological_sort_util(node, stack, visited)
        return stack
        
def find_shortest_path(graph, source):
    order = graph.topological_sort()
    #print("Topological Ordering")
    #while len(order) > 0:
    #    print(order.pop(), end=" ")
    
    distance = [float("inf")] * graph.V
    distance[source] = 0
    # Process vertices in topological ordering
    while order:
        node = order.pop()
        for neighbor, weight in graph.adjList[node]:
            if distance[neighbor] > distance[node] + weight:
                distance[neighbor] = distance[node] + weight
    print("\nShortest Distances for Source are")
    print(distance)
g = Graph(6)
g.add_edge(0,1,5)
g.add_edge(0,2,3)
g.add_edge(1,2,2)
g.add_edge(1,3,6)
g.add_edge(2,3,7)
g.add_edge(2,4,4)
g.add_edge(2,5,2)
g.add_edge(3,4,-1)
g.add_edge(4,5,-2)

find_shortest_path(g,0)
