from Graph import Graph
import collections

def bfs_cycle_detection(adjList):
    visited = set()

    def isCyclic(src, adjList):
        parent = {}
        q = collections.deque()
        q.append(src)
        visited.add(src)
        parent[src] = -1

        while q:
            node = q.popleft()
            for nei in adjList[node]:
                if nei not in visited:
                    q.append(nei)
                    parent[nei] = node
                    visited.add(nei)
                elif parent[node] != nei:
                    return True
        return False

    for node in adjList:
        if node not in visited:
            if isCyclic(node, adjList):
                return True
    return False

def dfs_cycle_detection(adjList):
    visited = set()

    def isCyclic(src, parent, adjList):
        visited.add(src)
        for nei in adjList[src]:
            if nei not in visited:
                if isCyclic(nei, src, adjList):
                    return True
            elif parent != nei:
                return True
            
        return False

    for node in adjList:
        if node not in visited:
            if isCyclic(node, -1, adjList):
                return True
    return False


def dfs_Cycle_Detection_Directed_graph_using_path_visited_set(adjList):
    visited = set()
    path_visited = set()

    def isCyclic(v):
        visited.add(v)
        path_visited.add(v)
        for nei in adjList[v]:
            if nei not in visited:
                if isCyclic(nei):
                    return True
            elif nei in path_visited:
                return True
        
        path_visited.remove(v)
        return False
    
    for node in list(adjList.keys()):
        if node not in visited:
            if isCyclic(node):
                return True
    return False

def dfs_Cycle_Detection_Directed_graph_using_flag_mapping(adjList, V):
    visited = [0] * V
    # will use flag,  0, 1, 2: 0: not processed, 1: Processed, 2: processing
    # if we find any in processing node in path then there is a cycle
    # same as path visited approach, but not using additional memory

    def isCyclic(v):
        if visited[v] == 2:
            return True
        visited[v] = 2

        for nei in adjList[v]:
            if visited[nei] != 1:
                if isCyclic(nei):
                    return True
        
        visited[v] = 1
        return False
    
    for node in list(adjList.keys()):
        if visited[node] == 0:
            if isCyclic(node):
                return True
    return False

if __name__ == "__main__":
    graph = Graph()

    edges = [[0, 1], [0, 4], 
        [0, 2], [1, 3], [1, 4], [2, 5],
        [2, 6], [3, 4], [7,8]]
    
    for u,v in edges:
        graph.add_edge(u,v)
    print("UnDirected Graph:", graph.adjList)

    print("\n1. Cycle Detection - BFS")
    print(bfs_cycle_detection(graph.adjList))
    print("\n2. Cycle Detection - DFS")
    print(dfs_cycle_detection(graph.adjList))

    graph1 = Graph()

    edges = [[0, 1], [0, 4], 
        [0, 2], [4,3], [2, 5],
        [2, 6], [5,3], [3,2]]
    
    for u,v in edges:
        graph1.add_edge_directed_graph(u,v)
    
    print("\nDirected Graph:", graph1.adjList)
    print("\n1. Cycle Detection - DFS using Path visited set")
    print(dfs_Cycle_Detection_Directed_graph_using_path_visited_set(graph1.adjList))
    print("\n2. Cycle Detection - DFS using processing flag")
    print(dfs_Cycle_Detection_Directed_graph_using_flag_mapping(graph1.adjList, 7))
    