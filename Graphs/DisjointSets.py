from collections import defaultdict
class Graph:
    def __init__(self, V):
        self.V = V
        self.adjList = defaultdict(list)
    
    def add_edge(self, v1, v2):
        self.adjList[v1].append(v2)
        self.adjList[v2].append(v1)

class DisjointSet:
    def __init__(self, n):
        self.parent = [i for i in range(n+1)]
        self.rank = [0] * (n+1)
    
    def find(self, u):
        if self.parent[u] == u:
            return u
        self.parent[u] = self.find(self.parent[u])
        return self.parent[u]
    
    def union(self, u, v):
        u = self.find(u)
        v = self.find(v)
        if u != v:
            if self.rank[u] > self.rank[v]:
                self.parent[v] = u
            elif self.rank[u] < self.rank[v]:
                self.parent[u] = v
            else:
                self.parent[v] = u
                self.rank[u] += 1

# Example graph (3 disjoint sets)
"""
 1---2    4----5----6     7----8----9-----3
"""
n=9 # number of nodes in a graph
# Build graph
g = Graph(n)
g.add_edge(1,2)
g.add_edge(5,4)
g.add_edge(5,6)
g.add_edge(8,7)
g.add_edge(8,9)
g.add_edge(9,3)
print(g.adjList)
# initializes the disjoint set for n nodes
dsu = DisjointSet(n)
for node, edge in g.adjList.items():
    for item in edge:
        dsu.union(node, item)

# check if 7 and 4 are in same set
if dsu.find(4) == dsu.find(7):
    print("Yes")
else:
    print("No")

# check if 6 and 4 are in same set
if dsu.find(4) == dsu.find(6):
    print("Yes")
else:
    print("No")

# check if 1 and 3 are in same set
if dsu.find(1) == dsu.find(3):
    print("Yes")
else:
    print("No")