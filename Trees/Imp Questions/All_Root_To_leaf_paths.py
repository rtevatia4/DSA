"""
https://www.techiedelight.com/print-all-paths-from-root-to-leaf-nodes-binary-tree/
"""
from Node import Node

def isLeaf(root):
    if root.left is None and root.right is None:
        return True
    return False

def print_root_to_leaf_paths(root, path):
    if root is None:
        return None
    
    path.append(root.val)

    if isLeaf(root):   # always try to use these kind of helper functions for readability
        print(path)

    print_root_to_leaf_paths(root.left, path)
    print_root_to_leaf_paths(root.right, path)
    #print(path)
    path.pop()

# Driver Code
if __name__ == '__main__':

    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
     
    path = []
    # print kth ancestor of given node
    print_root_to_leaf_paths(root, path)
    print(path)

"""
def printRootToLeafPathIterative(root):
 
    # base case
    if not root:
        return
 
    # create an empty stack to store a pair of tree nodes and
    # its path from the root node
    stack = deque()
 
    # push the root node
    stack.append((root, ""))
 
    # loop till stack is empty
    while stack:
 
        # pop a node from the stack and push the data into the output stack
        curr, path = stack.pop()
 
        # add the current node to the existing path
        path += (" —> " if path else "\n") + str(curr.data)
 
        # print the path if the node is a leaf
        if curr.left is None and curr.right is None:
            print(path, end='')
 
        # push the left and right child of the popped node into the stack
        if curr.right:
            stack.append((curr.right, path))
 
        if curr.left:
            stack.append((curr.left, path))
"""