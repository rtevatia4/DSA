"""
Binary Tree Boundary traversal.

Traversing all the nodes around the boundary of the tree
                        1
                2              3
            4       6       7       8
          5   9

o/p - 1 2 4 5 9 6 7 8 3

                        1
                2           4
              3   5           7
                 6 8            9 
                              10 11
o/p - 1 2 3 6 8 10 11 9 7 4
"""

from Node import Node

def print_left_boundary(root):
    if root:
        if not (root.left is None and root.right is None):
            print(root.val, end= " ")
            print_left_boundary(root.left)

def print_right_boundary(root):
    if root:
        if not (root.left is None and root.right is None):
            print_right_boundary(root.right)
            print(root.val, end= " ")
        
def print_leaves(root):
    if root:
        print_leaves(root.left)
        if root.left is None and root.right is None:
            print(root.val, end= " ")
        print_leaves(root.right)

def boundary_traversal(root):
    if root is None:
        return root
    print(root.val, end=" ")
    print_left_boundary(root.left)

    print_leaves(root.left)
    print_leaves(root.right)

    print_right_boundary(root.right)


if __name__== "__main__":
    root1 = Node(1)
    root1.left = Node(2)
    root1.right = Node(3)
    root1.left.left = Node(4)
    root1.left.left.left = Node(5)
    root1.left.right = Node(6)
    root1.right.left = Node(7)
    root1.right.right = Node(8)
    root1.right.right.right = Node(9)
    """
                        1
                2              3
            4       6       7       8
        5                              9
    """
    boundary_traversal(root1)
    print("\ncase 2")
    root = Node(20)
    root.left = Node(8)
    root.left.left = Node(4)
    root.left.right = Node(12)
    root.left.right.left = Node(10)
    root.left.right.right = Node(14)
    root.right = Node(22)
    root.right.right = Node(25)
    boundary_traversal(root)