from dsu import DSU
class Graph:
    def __init__(self, V):
        self.V = V
        self.adjList = [[] for i in range(V+1)]
    
    def add_edge(self, u, v, w):
        self.adjList[u].append((v,w))
        self.adjList[v].append((u,w))

def mst_kruskals_algo(adj, V):
    dsu = DSU(6)
    edges = []
    for i in range(V+1):
        for v,w in adj[i]:
            edges.append([i,v,w])

    edges = sorted(edges, key=lambda x:x[2])

    mst_sum = 0
    mst_edges = []

    for u,v,w in edges:
        x = dsu.find(u)
        y = dsu.find(v)
        if x != y:
            mst_sum += w
            mst_edges.append([u,v,w])
            dsu.union(x,y)

    print("MST Cost is : ", mst_sum )
    print("MST edges are: ", mst_edges) 

if __name__ == "__main__":
    edges = [[1,2,7], [1,3,8], [2,3,3], [2,5,6], [3,5,4], [3,4,3], [5,4,2], [5,6,5], [4,6,2]]

    g = Graph(6)
    for u,v,w in edges:
        g.add_edge(u,v,w)
    
    print("1. Minimum Spanning Tree: Kruskals Algo:")
    mst_kruskals_algo(g.adjList, 6)