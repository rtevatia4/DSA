from typing import List
# Write any import statements here

def getMaxAdditionalDinersCount(N: int, K: int, M: int, S: List[int]) -> int:
  front, back = 0, 0
  num_of_available_seats = 0
  for i in range(1,N+1):
    front = i
    back = i
    if i not in S:
      valid = True
      while front < i+K and front < N:
        #print(front,i)
        if front+1 in S:
          valid = False
          break
        front+=1
      if not valid:
        continue
      #print(valid,i)
      while back > i-K and back > 1:
        if back-1 in S:
          valid = False
          break
        back -= 1
      #print("back",valid,i)
      if not valid:
        continue
      num_of_available_seats += 1
      S.append(i)
  return num_of_available_seats

print(getMaxAdditionalDinersCount(10,1,2,[2,6]))

print(getMaxAdditionalDinersCount(15,2,3,[11,6,14]))