print("Hello World")

power = 1
while power < 7:
    power = power<<1
print(power)


test = [1,1,2]
print(test)
print(test[2::])
from collections import defaultdict
graph = defaultdict(defaultdict)
graph['a']['b'] = 2
print(graph)