from typing import List
import heapq
class Solution:
    def shortestPath(self,n:int, m:int, edges:List[List[int]] )->List[int]:
        adj = [[] for i in range(n+1)]
        for edge in edges:
            e1,e2,w = edge[0],edge[1],edge[2]
            adj[e1].append([e2,w])
            adj[e2].append([e1,w])
        # print(adj)\
        parent = [i for i in range(n+1)]
        distance = [1e9] * (n+1)
        distance[1] = 0
        heap = [(0,1)]
        while heap:
            dist, node = heapq.heappop(heap)
            for nei in adj[node]:
                new_dist = dist + nei[1]
                if new_dist < distance[nei[0]]:
                    heapq.heappush(heap,(new_dist,nei[0]))
                    distance[nei[0]] = new_dist
                    parent[nei[0]] = node
        # print(prev,distance)
        if distance[n] == 1e9:
            return [-1]
        # print(distance)
        result = []
        curr = n
        while parent[curr] != curr:
            result.append(curr)
            curr = parent[curr]
        result.append(1)
        return result[::-1]

if __name__ == "__main__":
    for _ in range(int(input())):
        n,m = map(int,input().split())
        edges = []
        for i in range(m):
            a,b,c = map(int,input().split())
            edges.append([a,b,c])
        
        obj = Solution()
        res = obj.shortestPath(n, m, edges)
        for e in res:
            print(e,end=" ")
        print()