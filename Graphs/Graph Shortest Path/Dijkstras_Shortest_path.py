from collections import defaultdict
import heapq

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.adjList = defaultdict(list)
    
    def add_edge(self, v1, v2, w):
        self.adjList[v1].append((v2,w))

def dijkstra_shortest_path(graph, V, source, destination=None):
    distance = [float("inf")] * V
    distance[source] = 0
    visited = set()
    
    pq = [(0, source, ())]
    
    while pq:
        curr_dist, node, path = heapq.heappop(pq)
        
        visited.add(node)
        path += (node, )
        if node == destination:
            print(curr_dist, path)
            return
        for neighbor, weight in graph.adjList[node]:
            if neighbor in visited:
                continue
            new_dist = curr_dist + weight
            if new_dist < distance[neighbor]:
                distance[neighbor] = new_dist
                heapq.heappush(pq, (new_dist, neighbor, path))
    
    # This distance list will be printed if we don't provide destination and we can find cost of reaching a 
    # a specific vertex using the distance list
    print(distance)
    #print(path)

g = Graph(5)
g.add_edge(0,1,4)
g.add_edge(0,2,1)
g.add_edge(1,3,1)
g.add_edge(2,1,2)
g.add_edge(2,3,5)
g.add_edge(3,4,3)

dijkstra_shortest_path(g, g.V, 0)
print("Path and cost from 0--> 4")
dijkstra_shortest_path(g, g.V, 0, 4)