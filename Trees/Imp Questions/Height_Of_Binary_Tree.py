"""
Given Binary Tree. FInd the height of the Binary Tree
Time Complexity - O(n), Space Complexity - O(h) as we are using Recursion (call Stack) but O(n) space in case of skewed tree
"""
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class Tree:
    def height(self, root):
        if root is None:
            return 0
        left = self.height(root.left)
        right = self.height(root.right)
        return max(left, right) + 1

if __name__== "__main__":
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
    print("Height of the Given Tree is:")
    tree = Tree()
    print(tree.height(root))