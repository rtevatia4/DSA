"""
https://www.geeksforgeeks.org/kth-ancestor-node-binary-tree/
"""
from Node import Node

def find_kth_Ancestor_Iterative_Solution(root, node1):
    if root is None:
        return None
    stack = []
    stack.append((root,[]))
    while stack:
        node, path = stack.pop()

        path.append(node.val)
        if node.val == node1:
            return path
        if node.left is None and node.right is None:
            path.pop()

        if node.left:
            stack.append((node.left, path))
        if node.right:
            stack.append((node.right, path))
    
    #if node == root.val:
    #    pass

# Driver Code
if __name__ == '__main__':

    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
     
    print("Test Case 1")
    k = 2
    node = 5
    # print kth ancestor of given node
    path = find_kth_Ancestor_Iterative_Solution(root, node)
    print(path[len(path)-1-k])

    print("Test Case 2")
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
    k = 1
    node = 5
    # print kth ancestor of given node
    path = find_kth_Ancestor_Iterative_Solution(root1, node)
    print(path[len(path)-1-k] if path else -1)