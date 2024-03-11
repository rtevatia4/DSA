"""
https://www.hackerrank.com/challenges/torque-and-development/problem

Will solve using BFS and Disjoin set
STDIN       Function
-----       --------
2           q = 2
3 3 2 1     n = 3, cities[] size m = 3, c_lib = 2, c_road = 1
1 2         cities = [[1, 2], [3, 1], [2, 3]]
3 1
2 3
6 6 2 5     n = 6, cities[] size m = 6, c_lib = 2, c_road = 5
1 3         cities = [[1, 3], [3, 4],...]
3 4
2 4
1 2
2 3
5 6
Sample Output

4
12
"""

#!/bin/python3

import math
import os
import random
import re
import sys
from collections import defaultdict, deque
#
# Complete the 'roadsAndLibraries' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER c_lib
#  3. INTEGER c_road
#  4. 2D_INTEGER_ARRAY cities
#

# using BFS

def roadsAndLibraries(n, c_lib, c_road, cities):
    if c_lib < c_road: return c_lib * n
    g, seen, ans = defaultdict(set), set(), 0
    csize = []
    for i,j in cities:
        g[i].add(j) 
        g[j].add(i)
    def bfs_get_clusters(node):
        queue = deque()
        queue.append(node)
        size = 1
        seen.add(node)
        while queue:
            n = queue.popleft()
            for nei in g[n]:
                if nei not in seen:
                    queue.append(nei)
                    seen.add(nei)
                    size +=1
        return size
    components = 0
    for nodes in range(1,n+1):
        if nodes not in seen:
            components +=1
            size = bfs_get_clusters(nodes)
            csize.append(size)
    #print(csize)
    return (components*c_lib + sum((x-1)*c_road for x in csize))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        m = int(first_multiple_input[1])

        c_lib = int(first_multiple_input[2])

        c_road = int(first_multiple_input[3])

        cities = []

        for _ in range(m):
            cities.append(list(map(int, input().rstrip().split())))

        result = roadsAndLibraries(n, c_lib, c_road, cities)

        fptr.write(str(result) + '\n')

    fptr.close()

"""disjoint set solution
"""
"""import sys


q = int(input().strip())
for a0 in range(q):
    n,m,x,y = input().strip().split(' ')
    n,m,x,y = [int(n),int(m),int(x),int(y)]
    
    par = [i for i in range(n + 1)]
    count = [1] * (n + 1)
    def find(a):
        if a != par[a]: par[a] = find(par[a])
        return par[a]
    def union(a, b):
        a = find(a)
        b = find(b)
        if a != b:
            par[b] = a
            count[a] += count[b]
    
    for a1 in range(m):
        city_1,city_2 = input().strip().split(' ')
        city_1,city_2 = [int(city_1),int(city_2)]
        union(city_1, city_2)
    
    ans = 0
    for a1 in range(1, n + 1):
        if a1 == par[a1]: ans += min(x * count[a1], x + y * (count[a1] - 1))
    print(ans)


    def roadsAndLibraries(n, c_lib, c_road, cities):
    max_cost = n*c_lib
    if c_road >= c_lib:
        return max_cost
        
    parent = [i for i in range(n+1)]
    def find(u):
        if parent[u] == u:
            return u
        parent[u] = find(parent[u])
        return parent[u]
    
    for x,y in cities:
        u=find(x)
        v=find(y)
        if u!=v:
            parent[v] = u
            max_cost -= c_lib 
            max_cost += c_road

    return max_cost 

## DFS

    def roadsAndLibraries(n, c_lib, c_road, cities):
    if c_road >= c_lib:
        return n*c_lib
    
    g = [[] for i in range(n+1)]
    for x,y in cities:
        g[x].append(y)
        g[y].append(x)
    
    components = 0
    comp_size = []
    visited = set()
    
    def dfs(node):
        visited.add(node)
        s = 1
        for nei in g[node]:
            if nei not in visited:
                s += dfs(nei)
        return s
                
    for v in range(1,n+1):
        if v not in visited:
            components += 1
            size = dfs(v)
            comp_size.append(size)
            
    min_cost = 0
    min_cost += components*c_lib
    for s in comp_size:
        min_cost += (s-1)*c_road
        
    return min_cost 
"""