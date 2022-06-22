"""
https://www.interviewbit.com/problems/knight-on-chess-board/
https://www.spoj.com/problems/NAKANJ/
"""
import collections

def knight(A, B, C, D, E, F):
    directions = [[-2,-1], [-2,1], [-1,2], [1,2], [2,1], [2,-1], [1,-2], [-1,-2]]
    board = [[-1]*(B+1) for _ in range(A+1)]
    board[C][D] = 0
    board[E][F] = 1
    #print(board)
    queue = collections.deque()
    queue.append((C,D, 0))
    visited = set((C,D))
    steps = 0
    while queue:
        gridr, gridc, steps = queue.popleft()
        if board[gridr][gridc] == 1:
            return steps
        for nr, nc in directions:
            r = nr+gridr
            c = nc + gridc
            #print(r,c)
            if r in range(1,A+1) and c in range(1,B+1) and (r,c) not in visited:
                queue.append((r,c, steps+1))
                visited.add((r,c))

    return -1

print(knight(8,8,1,1,8,8))