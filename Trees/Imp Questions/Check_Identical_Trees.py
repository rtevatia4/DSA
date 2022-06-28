from Node import Node
from Height_Of_Binary_Tree import Tree

def is_identical(root1, root2):   #O(n) time
    if not root1 and not root2:
        return True
    elif root1 and not root2:
        return False
    elif not root1 and root2:
        return False
        
    if root1.val == root2.val and is_identical(root1.left, root2.left) and is_identical(root1.right, root2.right):
        return True
    else:
        return False

if __name__== "__main__":
    root1 = Node(1)
    root1.left = Node(2)
    root1.right = Node(3)
    root1.left.left = Node(4)
    root1.left.left.left = Node(5)
    root1.left.right = Node(6)
    root1.right.left = Node(7)
    root1.right.right = Node(8)
    """
                        1
                2              3
            4       6       7       8
        5
    """
    root2 = Node(1)
    root2.left = Node(2)
    root2.right = Node(3)
    root2.left.left = Node(4)
    root2.left.left.left = Node(5)
    root2.left.right = Node(6)
    root2.right.left = Node(7)
    root2.right.right = Node(8)
    """
                        1
                2              3
            4       6       7       8
        5
    """
    print(is_identical(root1,root2))