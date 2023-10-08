class Node:
    def __init__(self, val):
        self.val = val
        self.right = None
        self.left = None


def BFT(root):
    if root is None:
        return
    q = []
    q.append(root)
    while q:
        node = q.pop(0)
        print(node.val, end=" ")
        if node.left:
            q.append(node.left)
        if node.right:
            q.append(node.right)
    return

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(5)
root.left.right = Node(4)

print("Level Order Traversal (BFT) of binary tree is -")
BFT(root)