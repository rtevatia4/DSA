import collections
import heapq

class Graph:
    def __init__(self, V):
        self.V = V
        self.adjList = [[] for i in range(V)]
    
    def add_edge(self, u, v):
        self.adjList[u].append(v)
        self.adjList[v].append(u)
    
    def add_edge_weighted(self, u, v, w):
        self.adjList[u].append((v,w))
        self.adjList[v].append((u,w))

def get_shortest_path(src, destination, adjList, V):
    parent = [-1] * V
    visited = [False] * V

    def build_path(v, adj):
        q = collections.deque()
        q.append(v)
        parent[v] = -1
        visited[v] = True
        while q:
            node = q.popleft()
            for nei in adj[node]:
                if not visited[nei]:
                    q.append(nei)
                    parent[nei] = node
                    visited[nei] = True
    
    for node in range(V):
        if not visited[node]:
            build_path(node, adjList)
    print(parent)
    path = []
    while destination != src:
        destination = parent[destination]
        path.append(destination)
    
    for i in path[::-1]:
        print(i, end="->")

def get_shortest_distance(src, V, adj):
    distance = [float("inf")] * V
    distance[src] = 0
    q = collections.deque()
    q.append((src,0))
    
    while q:
        node, dis = q.popleft()
        for nei in adj[node]:
            if distance[nei] > dis+1:
                distance[nei] = dis+1
                q.append((nei,dis+1))
    
    print(distance)


def shortest_distance_dijkstra_using_heap(V, adj, src):
    distance = [float("inf")] * V
    visited = set()
    distance[src] = 0

    heap = [(0,src)]
    while heap:
        curr_dis, node = heapq.heappop(heap)
        visited.add(node)
        for nei,w in adj[node]:
            # if nei in visited:
            #     continue
            new_dist = curr_dis + w
            if distance[nei] > new_dist:
                heapq.heappush(heap, (new_dist, nei))
                distance[nei] = new_dist
    
    print(distance)

if __name__ == "__main__":
    edges = [[0, 1], [0, 4], 
        [0, 2], [1, 3],
        [1, 4], [2, 5],
        [2, 6], [3, 4], [7,8]]
    
    g = Graph(9)
    for u,v in edges:
        g.add_edge(u,v)

    
    print("Undirected Graph is: ", g.adjList)
    print("\n1. Shortest Path:")
    print("\n1. Shortest Path from 0 to 3:")
    get_shortest_path(0,3,g.adjList,9)

    print("\n2. Shortest Distance using BFS:")
    get_shortest_distance(0,9,g.adjList)

    edges = [[0, 1,2], [0, 4,3], 
        [0, 2,1], [1, 3,4],
        [1, 4,5], [2, 5,3],
        [2, 6,4], [3, 4,6]]
    
    g1 = Graph(7)
    for u,v,w in edges:
        g1.add_edge_weighted(u,v,w)
    
    print("\nUndirected Graph with Weights is: ", g1.adjList)
    print("\n3. Shortest Distance using Dijkstra Algo (using heap):")
    shortest_distance_dijkstra_using_heap(7,g1.adjList, 0)