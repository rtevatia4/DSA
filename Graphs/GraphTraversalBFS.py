
from GraphAdjList import Graph
import collections

def bfs(graph, vertex):
    visited = [False] * graph.vertices
    queue = collections.deque()
    visited[vertex] = True
    queue.append(vertex)
    while queue:
        node = queue.popleft()
        print(node, "-->", end=" ")
        for neighbor in graph.adjList[node]:
            if not visited[neighbor]:
                queue.append(neighbor)
                visited[neighbor] = True

def main():
    g = Graph(6)
    g.add_edge(0,4)
    g.add_edge(4,0)
    g.add_edge(4,1)
    g.add_edge(4,2)
    g.add_edge(1,4)
    g.add_edge(1,5)
    g.add_edge(2,4)
    g.add_edge(2,3)
    g.add_edge(3,2)
    g.add_edge(3,5)
    g.add_edge(5,1)
    g.add_edge(5,3)

    g.print_graph()
    #visited = [False] * g.vertices

    print("\nBFS Traversal\n")
    bfs(g,0)

if __name__ == "__main__":
    main()
    
