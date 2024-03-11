import collections

def shortestPath(n, edges, src):
    adj = [[] for i in range(n)]
    for v1,v2 in edges:
        adj[v1].append(v2)
        adj[v2].append(v1)

    distance = [float("inf")] * n
    q = collections.deque()
    q.append((src,0))
    distance[src] = 0
    visited = set()
    visited.add(src)
    while q:
        node,d = q.popleft()
        for nei in adj[node]:
            if nei not in visited:
                visited.add(nei)
                q.append((nei,d+1))
                distance[nei] = d+1
    print(distance)

shortestPath(7,[(0, 1), (1, 2), (2, 3), (2, 5), (3, 5),(3, 4), (3, 6)], 1)
