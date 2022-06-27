
class Graph():
    def __init__(self, vertices):
        self.V = vertices
        self.graph = []
    
    def add_edge(self, v1, v2, w):
        self.graph.append((v1,v2,w))
    
    def find(self, parent, u):
        if parent[u] == u:
            return u
        parent[u] = self.find(parent, parent[u])
        return parent[u]
    
    def union(self, parent, rank, u, v):
        u = self.find(parent, u)
        v = self.find(parent, v)
        if u != v:
            if rank[u] > rank[v]:
                u,v = v,u
            parent[u] = v
            if rank[u] == rank[v]:
                rank[u] += 1
    
    def kruskals_MST(self):
        self.graph = sorted(self.graph, key=lambda x:x[2])
        result = []
        parent = [i for i in range(self.V)]
        rank = [0] * self.V
        e = 0
        vertex = 0
        while e < self.V-1:
            u, v, w = self.graph[vertex]
            vertex += 1
            x = self.find(parent, u)
            y = self.find(parent, v)
            if x != y:
                e += 1
                result.append([u, v, w])
                self.union(parent, rank, x, y)
        
        min_cost = 0
        for u,v,w in result:
            min_cost += w
            print("%d----%d----%d"%(u,v,w))
        print("Minimum Cost: ", min_cost)

g = Graph(4)
g.add_edge(0,1,10)
g.add_edge(0,2,6)
g.add_edge(0,3,5)
g.add_edge(1,3,15)
g.add_edge(2,3,4)
g.kruskals_MST()
