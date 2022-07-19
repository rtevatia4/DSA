"""
https://www.lintcode.com/problem/663/
You are given a m x n 2D grid initialized with these three possible values.

-1 - A wall or an obstacle.
0 - A gate.
INF - Infinity means an empty room. We use the value 2^31 - 1 = 2147483647 to represent INF as you may assume that the distance to a gate is less than 2147483647.
Fill each empty room with the distance to its nearest gate. If it is impossible to reach a Gate, that room should remain filled with INF

Input:
[[2147483647,-1,0,2147483647],[2147483647,2147483647,2147483647,-1],[2147483647,-1,2147483647,-1],[0,-1,2147483647,2147483647]]
Output:
[[3,-1,0,1],[2,2,1,-1],[1,-1,2,-1],[0,-1,3,4]]

Explanation:
the 2D grid is:
INF  -1  0  INF
INF INF INF  -1
INF  -1 INF  -1
  0  -1 INF INF
the answer is:
  3  -1   0   1
  2   2   1  -1
  1  -1   2  -1
  0  -1   3   4
"""
import collections
from typing import ( List, )
# Approach 1 - single source BFS
def bfs(r,c, ROWS, COLS):
    visited = set()
    q = collections.deque()
    visited.add((r,c))
    q.append((r,c, 0))
    directions = [[0,1], [1,0], [0,-1], [-1,0]]
    curr_dist = 0
    while q:
        row, col, dist = q.popleft()
        #curr_dist+=1
        for dr, dc in directions:
            r = dr+row
            c=dc+col
            if r in range(ROWS) and c in range(COLS) and rooms[r][c] != -1 and rooms[r][c] != 0 and (r,c) not in visited:
                visited.add((r,c))
                q.append((r,c,dist+1))
                if rooms[r][c] > dist+1:
                    rooms[r][c] = dist+1
    #print(rooms)

def walls_and_gates(rooms: List[List[int]]):
    ROWS, COLS = len(rooms) , len(rooms[0])
    for r in range(ROWS):
        for c in range(COLS):
            if rooms[r][c] == 0:
                bfs(r,c, ROWS, COLS)
    print(rooms)

rooms = [[2147483647,-1,0,2147483647],[2147483647,2147483647,2147483647,-1],[2147483647,-1,2147483647,-1],[0,-1,2147483647,2147483647]]

walls_and_gates(rooms)

walls_and_gates([[0,-1],[2147483647,2147483647]])


# # Approach 2 - Multi source BFS
def walls_and_gates1(self, rooms: List[List[int]]):
        ROWS, COLS = len(rooms), len(rooms[0])
        visit = set()
        q = collections.deque()

        def addRooms(r, c):
            if (min(r, c) < 0 or r == ROWS or c == COLS or
                (r, c) in visit or rooms[r][c] == -1):
                return
            visit.add((r, c))
            q.append([r, c])
        
        for r in range(ROWS):
            for c in range(COLS):
                if rooms[r][c]== 0:
                    q.append([r,c])
                    visit.add((r,c))
        dist = 0
        while q:
            for i in range(len(q)):
                r, c = q.popleft()
                rooms[r][c] = dist
                addRooms(r + 1, c)
                addRooms(r - 1, c)
                addRooms(r, c + 1)
                addRooms(r, c - 1)
            dist += 1
