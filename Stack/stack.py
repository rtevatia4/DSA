class Stack:
    def __init__(self) -> None:
        self.stack = []
    
    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if self.is_empty():
            return
        return self.stack.pop()
    
    def peek(self):
        return self.stack[-1]

    def is_empty(self):
        #return len(self.stack) == 0
        return not self.stack

    def size(self):
        return len(self.stack)
    
    def __str__(self):
        return str(self.stack)

if __name__ == "__main__":
    stack = Stack()
    stack.push(7)
    stack.push(9)
    stack.push(10)
    stack.push(4)
    print(stack)
    print(stack.peek())
    print(stack.is_empty())
    print(stack.pop())
    print(stack)