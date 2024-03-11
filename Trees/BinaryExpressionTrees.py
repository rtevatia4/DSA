"""
Construct Expression Tree
"""

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = None
        self.right = None

class Tree:
    def inorder(self, root):
        if not root:
            return
        self.inorder(root.left)
        print(root.val, end="->")
        self.inorder(root.right)

if __name__ == "__main__":
    exp = "ABC*+D/"
    stack = []
    for c in exp:
        if c in ["*","+","-","/"]:
            node = Node(c)
            r = stack.pop()
            l = stack.pop()
            node.left = l
            node.right = r
            stack.append(node)
        else:
            stack.append(Node(c))
    print("Inorder of expression tree is: ")
    tree = Tree()
    tree.inorder(stack.pop())