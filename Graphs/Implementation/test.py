def topo_ordering_dfs(adjList):
    visited = set()
    ordering = []

    def dft(v):
        nonlocal visited, ordering  # Use nonlocal to access variables in the outer function

        visited.add(v)

        for nei in adjList[v]:
            if nei not in visited:
                dft(nei)

        ordering.insert(0, v)  # Correct the placement of this line

    for node in adjList:
        if node not in visited:
            dft(node)

    return ordering  # Return the final ordering

# Example usage:
# Assuming adjList is a dictionary representing the adjacency list of a directed graph
adjList = {
    'A': ['B', 'C'],
    'B': ['D'],
    'C': ['D'],
    'D': []
}

result = topo_ordering_dfs(adjList)
print("Topological Ordering:", result)