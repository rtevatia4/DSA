"""
https://www.hackerrank.com/challenges/journey-to-the-moon/problem

Using disjoint Set Union
"""
"""
5 3
0 1
2 3
0 4
Sample Output 0
6
"""
import os
import sys
import collections

class DSU:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [1] * n
    
    def find(self, x):
        if x == self.parent[x]:
            return x
        self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, u, v):
        u = self.find(u)
        v = self.find(v)
        if u != v:
            ranku = self.rank[u]
            rankv = self.rank[v]
            if ranku > rankv:
                self.parent[v] = u
            elif ranku < rankv:
                self.parent[u] = v
            else:
                self.parent[v] = u
                self.rank[u] += 1

def journeyToMoon(n, astronaut):
    csize = []
    dsu = DSU(n)
    
    for v1,v2 in astronaut:
        dsu.union(v1,v2)
    components = {}
    for node, c in enumerate(dsu.parent):
        components[dsu.find(c)] = 1 + components.get(dsu.find(c), 0)
    num_of_components = len(components)
    print(num_of_components, components)
    for key, val in components.items():
        csize.append(val)
    sums = 0
    result = 0 
    for size in csize:
        result += size*sums
        sums+=size

    return result
    """for vertices in range(n):
        if vertices not in visited:
            components += 1
            sizei = 1
            size = dfs(vertices)
            csize.append(size)
    result = 0
    sum1 = 0
    print(components, csize)
    for size in csize:
        result += size*sum1
        sum1 += size
    return result  """
    
if __name__ == '__main__':

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    p = int(first_multiple_input[1])

    astronaut = []

    for _ in range(p):
        astronaut.append(list(map(int, input().rstrip().split())))

    result = journeyToMoon(n, astronaut)

    print(result)
