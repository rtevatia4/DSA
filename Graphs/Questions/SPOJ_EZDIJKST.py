"""
https://www.spoj.com/problems/EZDIJKST/

"""
from collections import defaultdict
import heapq
from math import dist
from turtle import distance


class Graph:
    def __init__(self, V):
        self.V = V
        self.adjList = defaultdict(list)
    
    def add_edge(self, v1, v2, w):
        self.adjList[v1].append((v2,w))

def shortest_path_dijkstra(graph, V, source, destination):
    distance = [float("inf")] * (V+1)
    visited = set()
    distance[source] = 0
    heap = [(source,0)]
    while heap:
        node, curr_dist = heapq.heappop(heap)
        visited.add(node)
        for neighbor in graph.adjList[node]:
            #print(neighbor)
            if neighbor[0] in visited:
                continue
            new_dist = curr_dist + neighbor[1]
            if new_dist < distance[neighbor[0]]:
                distance[neighbor[0]] = new_dist
                heapq.heappush(heap, (neighbor[0], new_dist))
    if len(visited) != V:   # case where no path exist between source and destination
        return -1
    return distance[destination]

test_cases = int(input())
for _ in range(test_cases):
    V, E = map(int, input().split())
    g = Graph(V)
    for edge in range(E):
        v1, v2, w = map(int, input().split())
        g.add_edge(v1,v2,w)
    s, d = map(int, input().split())
    print(shortest_path_dijkstra(g, V, s, d))