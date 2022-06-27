class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for c in range(self.V)]
                         for r in range(self.V)]
    
    def get_minimum(self, key, mst):
        min_weight = float("inf")
        for i in range(self.V):
            if key[i] < min_weight and mst[i] == False:
                min_weight = key[i]
                min_index = i
        return min_index

    def prims_MST(self, start):
        key = [float("inf")] * self.V
        key[start] = 0
        parent = [None] * self.V
        parent[start] = -1
        mst = [False] * self.V
        for vertices in range(self.V):
            u = self.get_minimum(key, mst)
            print(key)
            mst[u] = True
            for v in range(self.V):
                if self.graph[u][v] > 0 and mst[v] == False and key[v] > self.graph[u][v]:
                    key[v] = self.graph[u][v]
                    parent[v] = u
        self.print_mst(parent)
    
    def print_mst(self, parent):
        print("Edge \t Weight")
        for i in range(1, self.V):
            print(parent[i], "-", i, "\t", self.graph[i][parent[i]])

g = Graph(5)
g.graph[0][1] = 2
g.graph[1][0] = 2
g.graph[0][3] = 6
g.graph[3][0] = 6
g.graph[1][2] = 3
g.graph[2][1] = 3
g.graph[1][4] = 5
g.graph[4][1] = 5
g.graph[1][3] = 8
g.graph[3][1] = 8
g.graph[2][4] = 7
g.graph[4][2] = 7
g.prims_MST(0)