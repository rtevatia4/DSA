"""
https://www.geeksforgeeks.org/check-if-a-given-binary-tree-is-sumtree/
"""

from Node import Node

def is_sum_tree(root):  # O(n) time
    if root is None:
        return (True, 0)
    if root.left is None and root.right is None:
        return (True, root.val)

    left = is_sum_tree(root.left)
    right = is_sum_tree(root.right)

    if left[0] and right[0] and root.val == left[1] + right[1]:
        return (True, 2*root.val)
    else:
        return (False, 0)

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
    print(is_sum_tree(root1)[0])

    root = Node(26)
    root.left = Node(10)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(6)
    root.right.right = Node(3)
    """   26
        /   \
      10     3
    /    \     \
  4      6      3  
  """
    
    print(is_sum_tree(root)[0])