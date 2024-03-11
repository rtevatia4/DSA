import collections
class Graph:
    def __init__(self):
        self.adjList = collections.defaultdict(list)
        self.parent = {}
        self.visited = set()
    
    def add_edge(self, u, v):
        self.adjList[u].append(v)
        self.adjList[v].append(u)
    
    def cycle_detection_bfs(self, source):
        self.visited.add(source)
        self.parent[source] = -1
        q = collections.deque()
        q.append(source)
        
        while q:
            node = q.popleft()
            for nei in self.adjList[node]:
                if nei not in self.visited:
                    q.append(nei)
                    self.parent[nei] = node
                    self.visited.add(nei)
                elif self.parent[node] != nei:
                    return True
        return False

if __name__ == "__main__":
    graph = Graph()
    graph.add_edge(1,2)
    graph.add_edge(2,3)
    graph.add_edge(4,5)
    graph.add_edge(5,6)
    graph.add_edge(5,7)
    graph.add_edge(6,8)
    graph.add_edge(8,7)
    graph.add_edge(8,9)
    print("Graph is:")
    print(graph.adjList)
    print("\nBFS Implementation\n")
    V = len(graph.adjList)
    isCycle = False
    for ver in range(V):
        if ver not in graph.visited:
            if graph.cycle_detection_bfs(ver):
                isCycle = True
                break
    if isCycle:
        print("Cycle is Present in the graph")
    else:
        print("No Cycle")