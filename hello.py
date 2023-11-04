print("Hello World")

power = 1
while power < 7:
    power = power<<1
print(power)


test = [1,1,2]
print(test)
print(test[2::])
import bisect
from collections import defaultdict
graph = defaultdict(defaultdict)
graph['a']['b'] = 2
print(graph)

num = [0,2,5,9]
print(bisect.bisect_left(num,8))

pos = "2736"

new_str = pos[0:1] + pos[1+1:]
print(pos,new_str)