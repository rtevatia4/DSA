import collections

class Graph:
    def __init__(self):
        self.adjList = {}
    
    def add_edge(self, fromVertex, toVertex):
        if fromVertex in self.adjList:
            self.adjList[fromVertex].append(toVertex)
        if toVertex in self.adjList:
            self.adjList[toVertex].append(fromVertex)
        if fromVertex not in self.adjList:
            self.adjList[fromVertex] = [toVertex]
        if toVertex not in self.adjList:
            self.adjList[toVertex] = [fromVertex]
    
    def print_graph(self):
        for vertex in self.adjList:
            print(vertex, "-->", "-->".join(str(edge) for edge in self.adjList[vertex]))
    
    def cycle_detection_bfs(self, start):
        visited = set()
        parent = [-1] * len(self.adjList)
        queue = collections.deque()
        visited.add(start)
        queue.append(start)
        while queue:
            node = queue.popleft()
            for neighbor in self.adjList[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
                    parent[neighbor] = node
                elif parent[node] != neighbor:
                    return True
        return False
    
    def check_cyclic_dfs_rec(self, visited, vertex, parent):
        visited[vertex] = True
        for neighbor in self.adjList[vertex]:
            if visited[neighbor] == False:
                if self.check_cyclic_dfs_rec(visited, neighbor, vertex):
                    return True
            elif parent != neighbor:
                return True
        return False

    def cycle_detection_dfs(self):
        visited = [False] * len(self.adjList)
        for vertex in self.adjList:
            if visited[vertex] == False:
                if self.check_cyclic_dfs_rec(visited, vertex, -1):
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
    graph.print_graph()
    print("\nBFS Implementation\n")
    if graph.cycle_detection_bfs(4):
        print("Cycle is Present")
    else:
        print("No Cycle")
    print("\nDFS Implementation\n")
    if graph.cycle_detection_dfs():
        print("Cycle is Present")
    else:
        print("No Cycle")