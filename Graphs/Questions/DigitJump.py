"""
https://www.codechef.com/problems/DIGJUMP
Input: 01234567890
out - 1   ( mininum number of jumps from S1 to Sn (0 to 0) is 1 here)

Input: 012134444444443
out: 4 
"""
# Idea is to use BFS here

from collections import defaultdict, deque
import queue


def ChefAndDigitJump(sequence):
    length = len(sequence)
    adjList = defaultdict(list)
    visited = [False] * length
    distance = [0] * length

    # creating avalue to index adjacencyList
    for index in range(length):
        adjList[sequence[index]].append(index)
    
    queue = deque([0])
    visited[0] = 1
    while queue:
        front = queue.popleft()
        if front == length-1:
            break
        val = sequence[front]
        for j in range(len(adjList[val])):
            next_index = adjList[val][j]
            if not visited[next_index]:
                visited[next_index] = True
                queue.append(next_index)
                distance[next_index] = distance[front] + 1
        
        # next conditions to cover s+1 and s-1 index visiting conditions
        if front-1 in range(length):
            if not visited[front-1]:
                visited[front-1] = True
                queue.append(front-1)
                distance[front-1] = distance[front] + 1

        if front+1 in range(length):
            if not visited[front+1]:
                visited[front+1] = True
                queue.append(front+1)
                distance[front+1] = distance[front] + 1
    
    return distance[-1]


s = "012134444444443"
print(ChefAndDigitJump(s))
s = "01234567890"
print(ChefAndDigitJump(s))
s = "02102016"
print(ChefAndDigitJump(s))