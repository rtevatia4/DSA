
def shortest_path_DAG_using_topo_sort(n, edges,src):
    adj = [[] for i in range(n)]
    distance = [float("inf")] * n

    for v1,v2,w in edges:
        adj[v1].append((v2,w))
    
    visited = set()
    topo_order = []

    def topo_rec(vertex):
        visited.add(vertex)
        for nei,w in adj[vertex]:
            if nei not in visited:
                topo_rec(nei)
        topo_order.append(vertex)

    for v in range(n):
        if v not in visited:
            topo_rec(v)

    print("Topo order", topo_order)

    distance[src] = 0
    while topo_order:
        node = topo_order.pop()
        for nei,w in adj[node]:
            if distance[nei] > distance[node]+w:
                distance[nei] = distance[node]+w
    print("distance", distance)



shortest_path_DAG_using_topo_sort(3,[[0, 1, 2], [1, 2, 3], [0, 2, 6]],0)