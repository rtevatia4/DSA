import heapq
class Graph:
    def __init__(self, V):
        self.V = V
        self.adjList = [[] for i in range(V)]
    
    def add_edge(self, u, v, w):
        self.adjList[u].append((v,w))

def get_shortest_distance_using_topo_sorting(adj, V, src):
    ordering = []
    visited = set()

    def topo_sort_dfs(adj, v):
        visited.add(v)
        for nei,w in adj[v]:
            if nei not in visited:
                topo_sort_dfs(adj, nei)

        ordering.append(v)

    for i in range(V):
        if i not in visited:
            topo_sort_dfs(adj, i)

    print("\nReverse Topo Ordering:", ordering)

    distance = [float("inf")] * V
    distance[src] = 0

    while ordering:
        node = ordering.pop()
        for nei, w in adj[node]:
            if distance[nei] > distance[node]+w:
                distance[nei] = distance[node]+w

    print("\n Distances are:", distance)

def shortest_distance_dijkstra_using_heap(adj, V, src):
    distance = [float("inf")] * V
    distance[src] = 0

    heap = [(0,src)]
    while heap:
        curr_dis, node = heapq.heappop(heap)
        for nei,w in adj[node]:
            new_dist = curr_dis + w
            if distance[nei] > new_dist:
                heapq.heappush(heap, (new_dist, nei))
                distance[nei] = new_dist
    
    print("Source:", src, "Distance:", distance)

def multi_source_shortest_distance_dijkstra_using_heap(adj, V):
    for i in range(V):
        shortest_distance_dijkstra_using_heap(adj, V, i)

def shortest_distance_bellmanford_algo(edges, V, src):
    distance = [float("inf")] * V
    distance[src] = 0

    for i in range(V-1):
        for u,v,w in edges:
            if distance[u] != float("inf") and distance[v] > distance[u]+w:
                distance[v] = distance[u]+w

    #Nth relaxation for finding negative cycle
    for u,v,w in edges:
         if distance[u] != float("inf") and distance[v] > distance[u]+w:
             print("Graph has negative cycle")
             return
    
    print(distance)


if __name__ == "__main__":
    graph = Graph(7)

    edges = [[0, 1, 3], [0, 4, 4], 
        [0, 2, 5], [4,3,2], [2, 5,4],
        [2, 6,6], [5,3,1], [6,5,-5]]
    
    for u,v,w in edges:
        graph.add_edge(u,v,w)
    
    print("DAG with Weights:", graph.adjList)

    print("\n1. Shortest Distance using Topo Sorting")
    get_shortest_distance_using_topo_sorting(graph.adjList, 7, 0)

    print("\n2. Shortest Distance using Dijkstra's Algo (using heap)")
    shortest_distance_dijkstra_using_heap(graph.adjList, 7, 0)

    print("\n3. Multi Source Shortest Distance using Dijkstra's Algo (using heap)")
    multi_source_shortest_distance_dijkstra_using_heap(graph.adjList, 7)

    print("\n4. Single Source Shortest Distance using BellmanFord Algo (N-1 relaxations)")
    shortest_distance_bellmanford_algo(edges, 7, 0)