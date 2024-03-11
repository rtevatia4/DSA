"""
We are given a binary tree T and a node V. We need to print a path from the root of the tree to the node.
"""
from Node import Node

def root_to_node_path(root,target):
    def dfs(node, target, path):
        if not node:
            return None

        # Append the current node to the path
        path.append(node.val)

        # If the current node is the target, return the path
        if node.val == target:
            return path

        # Recursively search in the left and right subtrees
        left_path = dfs(node.left, target, path.copy())
        right_path = dfs(node.right, target, path.copy())

        # Return the path if found in either subtree
        return left_path or right_path
    path = dfs(root, target, [])
    return path

def root_to_node_path_iterative(root,target):
    if not root:
        return []

    stack = [[root,[root.val]]]

    while stack:
        # print(stack)
        node, curr_path = stack.pop()
        if node.val == target:
            return curr_path
        
        if node.right:
            # print(node.right.val,curr_path)
            stack.append([node.right,curr_path+[node.right.val]])
        if node.left:
            stack.append([node.left,curr_path+[node.left.val]])

    # if path not found
    return []

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
    path = root_to_node_path(root1,6)
    print(path)
    print(root_to_node_path_iterative(root1,6))