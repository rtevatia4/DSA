# Cycle detection in an undirected graph
# will use DFS
"""
While performing DFS if we finds that any recursive call is going to an already visited vertex then there is a cycle

"""
import collections

class Graph:
    def __init__(self):
        self.adjList = collections.defaultdict(list)
    
    def add_edge(self, fromVertex, toVertex):
        if fromVertex in self.adjList:
            self.adjList[fromVertex].append(toVertex)
        else:
            self.adjList[fromVertex] = [toVertex]
    
    def print_graph(self):
        for vertex in self.adjList:
            print(vertex, "-->", "-->".join(str(edge) for edge in self.adjList[vertex]))
    
    def check_cyclic_dfs_rec(self, visited, vertex, dfs_visited):
        visited.add(vertex)
        dfs_visited.add(vertex)
        for neighbor in self.adjList[vertex]:
            if neighbor not in visited:
                if self.check_cyclic_dfs_rec(visited, neighbor, dfs_visited):
                    return True
            elif neighbor in dfs_visited:
                return True
        dfs_visited.remove(vertex)
        return False

    def cycle_detection_dfs(self):
        visited = set()
        dfs_visited = set()
        for vertex in self.adjList:
            if vertex not in visited:
                if self.check_cyclic_dfs_rec(visited, vertex, dfs_visited):
                    return True
        return False
    
if __name__ == "__main__":
    graph = Graph()
    graph.add_edge(1,2)
    graph.add_edge(2,3)
    graph.add_edge(2,4)
    graph.add_edge(3,7)
    graph.add_edge(3,8)
    graph.add_edge(4,5)
    graph.add_edge(5,6)
    graph.add_edge(6,4)
    graph.add_edge(8,7)
    
    graph.print_graph()
    
    print("\nCycle detection in Directed Graph - DFS\n")
    if graph.cycle_detection_dfs():
        print("Cycle is Present")
    else:
        print("No Cycle")