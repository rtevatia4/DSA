from Graph import Graph
import collections

def topo_ordering_dfs(adjList):
    visited = set()
    ordering = []

    def dft(v):
        visited.add(v)
        for nei in adjList[v]:
            if nei not in visited:
                dft(nei)
        
        ordering.insert(0, v)
    
    for node in list(adjList.keys()):
        if node not in visited:
            dft(node)

    print('->'.join(str(i) for i in ordering))

def topological_ordering_Kahns_algo(adjList, V):
    inDegree = [0] * V
    for node, edges in adjList.items():
        for edge in edges:
            inDegree[edge] += 1
    q = collections.deque()
    for i in range(len(inDegree)):
        if inDegree[i] == 0:
            q.append(i)
    
    ordering = []
    while q:
        node = q.popleft()
        ordering.append(node)
        for nei in adjList[node]:
            inDegree[nei] -= 1
            if inDegree[nei] == 0:
                q.append(nei)
    
    print('->'.join(str(i) for i in ordering))

if __name__ == "__main__":
    graph = Graph()

    edges = [[0, 1], [0, 4], 
        [0, 2], [4,3], [2, 5],
        [2, 6], [5,3]]
    
    for u,v in edges:
        graph.add_edge_directed_graph(u,v)
    
    print(graph.adjList)

    print("1. Topological Ordering using DFT")
    topo_ordering_dfs(graph.adjList)
    print("\n2. Topological Ordering using Kahns Algo")
    topological_ordering_Kahns_algo(graph.adjList, 7)

