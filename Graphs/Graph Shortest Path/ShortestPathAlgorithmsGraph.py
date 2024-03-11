import collections
class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.adjList = [[] for i in range(self.vertices)]
    
    def add_edge_undirected(self,u,v):
        self.adjList[u].append(v)
        self.adjList[v].append(u)

    def add_edge_with_weight_undirected(self,u,v,w):
        self.adjList[u].append((v,w))
        self.adjList[v].append((u,w))
    
    def add_edge_directed(self,u,v):
        self.adjList[u].append(v)

    def add_edge_with_weight_directed(self, u, v, w):
        self.adjList[u].append((v,w))
    
    def single_source_shortest_distance_unit_weight_bfs(self, source):
        distance = [float("inf")] * self.vertices
        distance[source] = 0

        q = collections.deque()
        q.append((source,0))

        while q:
            node,d = q.popleft()
            for nei in self.adjList[node]:
                if distance[nei] > d+1:
                    distance[nei] = d+1
                    q.append((nei,d+1))
        
        return distance
    
    def single_source_to_destination_shortest_path_bfs(self, source, destination):
        parent = [-1] * self.vertices
        visited = set()
        q=collections.deque()
        q.append(source)
        visited.add(source)

        while q:
            node = q.popleft()
            for nei in self.adjList[node]:
                if nei not in visited:
                    parent[nei] = node
                    q.append(nei)
                    visited.add(nei)
        
        # Build path from Parent List
        shortest_path = [destination]
        curr = destination
        while curr != source:
            curr = parent[curr]
            shortest_path.append(curr)
        
        return shortest_path[::-1]

    def topological_sort_rec(self, node, visited, stack):
        visited.add(node)
        for nei,weight in self.adjList[node]:
            if nei not in visited:
                self.topological_sort_rec(nei,visited,stack)
        
        stack.append(node)

    def shortest_distance_directed_graph_using_topological_sort(self,source):
        visited = set()
        stack = []
        for v in range(self.vertices):
            if v not in visited:
                self.topological_sort_rec(v, visited, stack)
        
        print("\tTopological Ordering of the Graph is:", stack[::-1])

        distance = [float("inf")] * self.vertices
        distance[source] = 0

        while stack:
            node = stack.pop()
            for nei,weight in self.adjList[node]:
                if distance[nei] > distance[node] + weight:
                    distance[nei] = distance[node] + weight
        
        return distance
            

if __name__ == "__main__":
    edges = [[0,1],[0,3],[3,4],[4 ,5],[5, 6],[1,2],[2,6],[6,7],[7,8],[6,8]]

    print("Building Undirected graph with Unit weight")
    undirected_graph = Graph(9)
    for edge in edges:
        undirected_graph.add_edge_undirected(edge[0],edge[1])
    
    print("Undirected graph with Unit weight:", undirected_graph.adjList)

    print("1. Get Single Source Shortest Distance using BFS (Unit Weight Graph)")
    print("\tDistances from Source 0:",undirected_graph.single_source_shortest_distance_unit_weight_bfs(0))

    print("2. Get Single Source Shortest Path to Destination using BFS (Unit Weight Graph)")
    print("\tPath from Source 0 to Destination 8:",undirected_graph.single_source_to_destination_shortest_path_bfs(0,8))

    edges = [[0,1,2],[0,4,1],[4,5,4],[4,2,2],[1,2,3],[2,3,6],[5,3,1]]
    print("-----------------------------------")
    print("Building Directed graph with weight")
    directed_graph = Graph(6)
    for edge in edges:
        directed_graph.add_edge_with_weight_directed(edge[0],edge[1],edge[2])
    print("Directed graph with weight:", directed_graph.adjList)
    print("3. Get Single Source Shortest Distance/Path in weighted DAG using Topological sort")
    print("\tDistances from Source 0:",directed_graph.shortest_distance_directed_graph_using_topological_sort(0))

    


