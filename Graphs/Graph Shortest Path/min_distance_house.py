"""
https://leetcode.com/problems/shortest-distance-from-all-buildings/description/
You are given an m x n grid grid of values 0, 1, or 2, where:

each 0 marks an empty land that you can pass by freely,
each 1 marks a building that you cannot pass through, and
each 2 marks an obstacle that you cannot pass through.
You want to build a house on an empty land that reaches all buildings in the shortest total travel distance. You can only move up, down, left, and right.

Return the shortest travel distance for such a house. If it is not possible to build such a house according to the above rules, return -1.

The total travel distance is the sum of the distances between the houses of the friends and the meeting point.

The distance is calculated using Manhattan Distance, where distance(p1, p2) = |p2.x - p1.x| + |p2.y - p1.y|.
Input: grid = [[1,0,2,0,1],[0,0,0,0,0],[0,0,1,0,0]]
Output: 7
Explanation: Given three buildings at (0,0), (0,4), (2,2), and an obstacle at (0,2).
The point (1,2) is an ideal empty land to build a house, as the total travel distance of 3+3+1=7 is minimal.
So return 7.

"""

class Solution:
    def shortestDistance(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        dir = [(0,1),(1,0),(-1,0),(0,-1)]
        distances = {(r,c):[0,0] for r in range(ROWS) for c in range(COLS) if grid[r][c] == 0 } # position:distance
        totalHouses = 0
        def bfs(row, col):
            visited = set()
            visited.add((row,col))
            q = collections.deque()
            q.append((row,col))
            level = 0
            while q:
                for i in range(len(q)):
                    posx,posy = q.popleft()
                    if grid[posx][posy] == 0:
                            distances[(posx,posy)][0] += level
                            distances[(posx,posy)][1] += 1 
                    for r,c in dir:
                        nr = r+posx
                        nc = c+posy
                        if nr not in range(ROWS) or \
                            nc not in range(COLS) or \
                            grid[nr][nc] == 2 or grid[nr][nc] == 1 or (nr,nc) in visited:
                            continue
                        visited.add((nr,nc))
                        q.append((nr,nc))

                level += 1

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    # print(distances)
                    totalHouses += 1
                    bfs(r,c)

        mindistance = float("inf")
        for dist, reach in distances.values():
            if reach == totalHouses:
                mindistance = min(mindistance,dist)

        return mindistance if mindistance < float("inf") else -1
        

