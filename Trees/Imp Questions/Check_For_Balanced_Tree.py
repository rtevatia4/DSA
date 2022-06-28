from Node import Node
from Height_Of_Binary_Tree import Tree

def check_balanced(root):   # Time complexity for this is O(n^2) because we are calling height function for each node
    if root is None:    # base case
        return True
    is_left_balanced = check_balanced(root.left)
    is_right_balanced = check_balanced(root.right)

    diff = abs(Tree().height(root.left) - Tree().height(root.right)) <= 1

    if is_left_balanced and is_right_balanced and diff:
        return True
    return False

def isBalanced_optimized(root): # here we are finding the height and checking balanced at the same time. Now Time Complexity O(n)
    if root is None:
        return (True,0)
    
    left = isBalanced_optimized(root.left)
    right = isBalanced_optimized(root.right)

    is_left_balanced = left[0]
    is_right_balanced = right[0]

    diff = abs(left[1] - right[1]) <= 1

    return (is_left_balanced and is_right_balanced and diff, max(left[1],right[1])+1)

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
    print(check_balanced(root))

    print(isBalanced_optimized(root))