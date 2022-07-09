"""
Top view of a binary tree is the set of nodes visible when the tree is viewed from the top. 
Given a binary tree, print the top view of it.
       1
    /     \
   2       3
  /  \    / \
 4    5  6   7
Top view of the above binary tree is
4 2 1 3 7

We can use the vertical ordering approach here. Can find nodes by horizontal distance and we just need one node per distance

"""
import collections
from Node import Node

def top_view(root):
    if not root:
        return root
    distance_map = {}
    queue = collections.deque([(root,0)])
    min_hd = 0
    max_hd = 0
    while queue:
        node, hd = queue.popleft()
        if hd not in distance_map:
            distance_map[hd] = [node.val]
        min_hd = min(min_hd, hd)
        max_hd = max(max_hd, hd)
        if node.left:
            queue.append((node.left, hd-1))
        if node.right:
            queue.append((node.right, hd+1))
    
    for i in range(min_hd, max_hd+1):
        print(distance_map[i][0], end=" ")

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
    
    
    print("\nTop view of a tree")
    print("\nTest Case 1")
    top_view(root1)

    """
       1
    /     \
   2       3
  /  \    / \
 4    5  6   7
    """
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)
    print("\nTest Case 2")
    top_view(root)