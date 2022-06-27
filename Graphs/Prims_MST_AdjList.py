# Prim's algorithm is a greedy algorithm that
# finds a minimum spanning tree
# for a weighted undirected graph.
#
# Time complexity: O(m * n)
import heapq

def prims(graph, root):
    key = [float("inf")] * len(graph)
    key[root] = 0
    parent = [None] * len(graph)
    parent[root] = -1
    visited = set()
    pq = [(0,root)]
    while pq:
        cost, node = heapq.heappop(pq)
        visited.add(node)
        for neighbor, weight in graph[node].items():
            if neighbor not in visited and key[neighbor] > weight:
                key[neighbor] = weight
                parent[neighbor] = node
                heapq.heappush(pq, (weight,neighbor))
    print(parent, "MST Cost:",sum(key))
    print("Edge \t Weight")
    for i in range(1, len(graph)):
        print(parent[i], "-", i, "\t", graph[parent[i]][i])

graph = {
            0 : {1:6, 2:8},
            1 : {4:11},
            2 : {3:9},
            3 : {},
            4 : {5:3},
            5 : {2:7, 3:4}
        }
prims(graph,0)