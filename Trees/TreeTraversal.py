import collections
from Node import Node

def inorder(root):
    if root:
        inorder(root.left)
        print(str(root.val) + "->", end=" ")
        inorder(root.right)

def preorder(root):
    if root:
        print(str(root.val) + "->", end="")
        preorder(root.left)
        preorder(root.right)

def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(str(root.val) + "->", end="")

def bfT(root):
    if not root:
        return
    queue = collections.deque()
    queue.append(root)
    while queue:
        node = queue.popleft()
        print(str(node.val) + "->", end=" ")
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    
    return


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.left.left = Node(5)
root.left.right = Node(6)
root.right.left = Node(7)
root.right.right = Node(8)
"""
                    1
            2              3
        4       6       7       8
    5
"""
print("Depth First Traversals: ")
print("1. Inorder Traversal")
inorder(root)
print("\n2. Preorder Traversal")
preorder(root)
print("\n3. postorder traversal")
postorder(root)

print("\n\nBreadth First/Level Order traversal")
bfT(root)