import collections
class Graph:
    def __init__(self, V):
        self.V = V
        self.adjList = collections.defaultdict(list)
    
    def add_edge(self, v1, v2):
        self.adjList[v1].append(v2)
        self.adjList[v2].append(v1)

class DSU:
    def __init__(self, V):
        self.parent = [i for i in range(V+1)]
        self.rank = [0 for i in range(V+1)]
    
    def find(self, u):
        if self.parent[u] == u:
            return u
        self.parent[u] = self.find(self.parent[u]) 
        return self.parent[u]

    def union(self, u, v):
        u = self.parent[u]
        v = self.parent[v]
        if u != v:
            if self.rank[u] > self.rank[v]:
                self.parent[v] = u
            elif self.rank[u] < self.rank[v]:
                self.parent[u] = v
            else:
                self.parent[v] = u
                self.rank[u] += 1

if __name__ == "__main__":
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

    dsu = DSU(n)

    for node, edges in g.adjList.items():
        for edge in edges:
            dsu.union(node,edge)
    
    if dsu.find(4) == dsu.find(7):
        print("4 and 7: Same Parent")
    else:
        print("4 and 7: parent not same")

    if dsu.find(9) == dsu.find(7):
        print("7 and 9: Same Parent")
    else:
        print("7 and 9: parent not same")