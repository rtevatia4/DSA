import collections
class Graph:
    def __init__(self):
        self.adjList = collections.defaultdict(list)
        self.visited = set()
    
    def add_edge(self, u, v):
        self.adjList[u].append(v)
        self.adjList[v].append(u)
    
    def cycle_detection_dfs(self, node, parent):
        self.visited.add(node)

        for nei in self.adjList[node]:
            if nei not in self.visited:
                if self.cycle_detection_dfs(nei,node):
                    return True
            elif parent != nei:
                return True
        return False

if __name__ == "__main__":
    graph = Graph()
    graph.add_edge(1,2)
    # graph.add_edge(1,3)
    graph.add_edge(2,3)
    graph.add_edge(4,5)
    graph.add_edge(5,6)
    graph.add_edge(5,7)
    graph.add_edge(6,8)
    graph.add_edge(8,7)
    graph.add_edge(8,9)
    print("Graph is:")
    print(graph.adjList)
    print("\nDFS Implementation\n")
    V = len(graph.adjList)
    isCycle = False
    for ver in range(V):
        if ver not in graph.visited:
            if graph.cycle_detection_dfs(ver, -1):
                isCycle = True
                break
    if isCycle:
        print("Cycle is Present in the graph")
    else:
        print("No Cycle")