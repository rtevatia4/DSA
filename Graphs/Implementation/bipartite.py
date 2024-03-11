from Graph import Graph
import collections

def check_bipartite(adjList, V):
    color = [-1] * V

    def isBipartite(v):
        q = collections.deque()
        q.append(v)
        color[v] = 0
        while q:
            node = q.popleft()
            for nei in adjList[node]:
                if color[nei] == -1:
                    q.append(nei)
                    color[nei] = color[node] ^ 1
                elif color[node] == color[nei]:
                    return False
        return True
    
    for node in adjList:
        if color[node] == -1:
            if not isBipartite(node):
                return False
    return True

if __name__ == "__main__":
    graph = Graph()

    edges = [[0, 1], [1, 2], [2,3], [2,4],
        [3,5], [4,6], [5,7],
        [6,7], [7,8],[8,9]]
    
    for u,v in edges:
        graph.add_edge(u,v)
    
    print(graph.adjList)
    print("Check Bipartite - Graph 1")
    print(check_bipartite(graph.adjList, 10))

    graph2 = Graph()

    edges = [[0, 1], [1, 2], [1,3], [2,4],
        [3,5], [4,6], [5,4],
        [6,7]]
    
    for u,v in edges:
        graph2.add_edge(u,v)

    print("\nCheck Bipartite - Graph 2")
    print(check_bipartite(graph2.adjList, 8))