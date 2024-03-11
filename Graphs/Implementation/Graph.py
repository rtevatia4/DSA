# Building a graph
import collections
class Graph:
    def __init__(self):
        self.adjList = collections.defaultdict(list)
    
    def add_edge(self,u,v):
        self.adjList[u].append(v)
        self.adjList[v].append(u)
    
    def add_edge_directed_graph(self,u,v):
        self.adjList[u].append(v)
    