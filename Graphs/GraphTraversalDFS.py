
from GraphAdjList import Graph

def dfs_iterative(graph, vertex):
    visited = set()
    stack = []
    stack.append(vertex)
    visited.add(vertex)
    while stack:
        node = stack.pop()
        print(node, "-->", end=" ")
        for neighbor in graph.adjList[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                stack.append(neighbor)

def dfs_recursive(graph, vertex, visited):
    if visited[vertex]:
        return 
    visited[vertex] = True
    print(vertex, "-->", end = " ")
    for adj in graph.adjList[vertex]:
        dfs_recursive(graph, adj, visited)

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
    visited = [False] * g.vertices
    print("\nDFS Recursive\n")
    dfs_recursive(g,0, visited)

    print("\nDFS Iterative\n")
    dfs_iterative(g,0)

if __name__ == "__main__":
    main()
    
