"""
Diameter - OR called as Width - Longest Path between 2 nodes
Longest path between two ending nodes
"""

from Node import Node
from Height_Of_Binary_Tree import Tree

def diameter(root):     # Time complexity is O(n^2) here because we are also calling the height function 
    if root is None:
        return 0
    left_diameter = diameter(root.left)
    right_diameter = diameter(root.right)
    combined_diameter = Tree().height(root.left) + 1 + Tree().height(root.right)
    return max(left_diameter, right_diameter, combined_diameter)

def diameter_optimized(root): # here we are finding the height and diameter at the same time. Now Time Complexity O(n)
    if root is None:
        return (0,0)
    
    left = diameter_optimized(root.left)
    right = diameter_optimized(root.right)

    left_diameter = left[0]
    right_diameter = right[0]
    combined_diameter = left[1] + right[1] + 1

    return (max(left_diameter, right_diameter, combined_diameter), max(left[1],right[1])+1)

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.left.left = Node(5)
root.left.right = Node(6)
root.right.left = Node(7)
root.right.right = Node(8)
print("Diameter of the Tree is")
"""
                        1
                2              3
            4       6       7       8
        5
"""
print(diameter(root))
print("Diameter of the Tree using optmized algo is")
print(diameter_optimized(root))
