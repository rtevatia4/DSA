"""
You are trapped in a Dungeon and you have to find the quickest(shortest) way out.
The Dungeon is composed of unit cubes which may or may not be filled with rocks.
It takes one minute to move one unit north, south, east and west.

"#" -> cell full of rock
"." -> Empty cell
S - Starting point
E - Exit cell
Given Grid:

S . . # . . . 
. # . . . # .
# . . . . . .
. . # # . . .
# . # E . # .

"""
import collections


def find_way_out(sr,sc):
    visited = set()
    queue = collections.deque()
    directions = [[0,1],[1,0],[0,-1],[-1,0]]
    queue.append((sr,sc))
    visited.add((sr,sc))
    num_of_moves = 0
    while queue:
        for i in range(len(queue)):
            gr,gc = queue.popleft()
            if grid[gr][gc] == "E":
                print("Found way out in %d moves" %(num_of_moves))
                return
            for x,y in directions:
                nx = gr+x
                ny = gc+y
                if nx in range(ROWS) and ny in range(COLS) and (nx,ny) not in visited and grid[nx][ny] != "#":
                    queue.append((nx,ny))
                    visited.add((nx,ny))
            
        num_of_moves += 1
    print("Can't find a way out")
    return
    
grid = [
["S", ".", ".", "#", ".", ".", "."], 
[".", "#", ".", ".", ".", "#", "."],
["#", ".", ".", ".", ".", ".", "."],
[".", ".", "#", "#", ".", ".", "."],
["#", ".", "#", "E", ".", "#", "."]
]

ROWS, COLS = len(grid), len(grid[0])
find_way_out(0,0)