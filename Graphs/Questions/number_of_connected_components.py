""""
LC 323 - Number of Connected Components in an Undirected Graph
You have a graph of n nodes. You are given an integer n and an array edges where edges[i] = [ai, bi] indicates that there is an edge between ai and bi in the graph.

Return the number of connected components in the graph.

"""

from collections import defaultdict

class Solution:
    def countComponents(self, n: int, edges) -> int:
        graph = defaultdict(list)
        for edge in edges:
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])
        count = 0
        visited = set()
        components = [-1] * n
        def dfs_count_components(vertex, count):
            visited.add(vertex)
            components[vertex] = count
            for nei in graph[vertex]:
                if nei not in visited:
                    dfs_count_components(nei,count)

        for i in range(n):
            if i not in visited:
                count += 1
                dfs_count_components(i, count)
        print(count)


s = Solution()
s.countComponents(5,[[0,1],[1,2],[3,4]])