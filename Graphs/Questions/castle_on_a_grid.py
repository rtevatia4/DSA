"""
https://www.hackerrank.com/challenges/one-month-preparation-kit-castle-on-the-grid/problem

You are given a square grid with some cells open (.) and some blocked (X). 
Your playing piece can move along any row or column until it reaches the edge of the grid or a blocked cell.
 Given a grid, a start and a goal, determine the minmum number of moves to get to the goal.

Example.
STDIN       FUNCTION
-----       --------
3           grid[] size n = 3
.X.         grid = ['.X.','.X.', '...']
.X.
...
0 0 0 2     startX = 0, startY = 0, goalX = 0, goalY = 2

Sample Output

3
"""

#!/bin/python3

import math
import os
import random
import re
import sys
import collections
#
# Complete the 'minimumMoves' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING_ARRAY grid
#  2. INTEGER startX
#  3. INTEGER startY
#  4. INTEGER goalX
#  5. INTEGER goalY
#

def minimumMoves(grid, startX, startY, goalX, goalY):
    ROWS = len(grid)
    COLS = len(grid[0])
    directions = [(0,1),(1,0),(0,-1),(-1,0)]
    q = collections.deque()
    q.append([startX,startY])
    visit = set()
    visit.add((startX,startY))
    moves = 0
    while q:
        moves += 1
        for i in range(len(q)):
            x,y = q.popleft()
            for dr,dc in directions:
                nr = x
                nc = y
                while True:
                    nr = dr+nr
                    nc = dc+nc
                    is_valid = (nr in range(ROWS) and nc in range(COLS) and grid[nr][nc] != "X")
                    if not is_valid:
                        break
                    else:
                        if nr==goalX and nc==goalY:
                            return moves
                        if (nr,nc) not in visit:
                            q.append([nr,nc])
                            visit.add((nr,nc))

                
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    grid = []

    for _ in range(n):
        grid_item = input()
        grid.append(grid_item)

    first_multiple_input = input().rstrip().split()

    startX = int(first_multiple_input[0])

    startY = int(first_multiple_input[1])

    goalX = int(first_multiple_input[2])

    goalY = int(first_multiple_input[3])

    result = minimumMoves(grid, startX, startY, goalX, goalY)

    fptr.write(str(result) + '\n')

    fptr.close()
