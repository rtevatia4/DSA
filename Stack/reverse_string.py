import stack

string = "learning the data structures"
reversed_string = ""
s = stack.Stack()
for char in string:
    s.push(char)
print(s)

while not s.is_empty():
    reversed_string += s.pop()

print(reversed_string)