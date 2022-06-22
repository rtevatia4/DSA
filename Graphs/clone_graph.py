# LeetCode 133
import collections

class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
    
class Graph(Node):
    def __init__(self, vertices):
        self.V = vertices
        self.adjList = [[] for i in range(vertices)]
    
class Solution:
    def cloneGraph(self, node:'Node') -> 'Node':
        if not node:
            return node
        visited = {}
        visited[node] = Node[node.val]
        queue = collections.deque([node])
        while queue:
            n = queue.popleft()
            for neighbor in n.neighbors:
                if neighbor not in visited:
                    visited[neighbor] = Node(neighbor.val)
                    queue.append(neighbor)
                visited[n].neighbors.append(visited[neighbor])
        return visited[node]