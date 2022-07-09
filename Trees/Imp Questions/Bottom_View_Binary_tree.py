"""
Bottom view of the binary tree
                        1
                2              3
            4       6       7       8
        5                              9

o/p - 5 4 2 7 3 8 9

We can use the vertical ordering approach here. Can find nodes by horizontal distance and we just need last node per distance

"""

from Node import Node
from collections import deque, defaultdict

def bottom_view(root):
    if not root:
        return root
    distance_map = defaultdict(list)
    queue = deque([(root,0)])
    min_hd = 0
    max_hd = 0
    while queue:
        node, hd = queue.popleft()
        distance_map[hd].append(node.val)
        min_hd = min(min_hd, hd)
        max_hd = max(max_hd, hd)
        if node.left:
            queue.append((node.left, hd-1))
        if node.right:
            queue.append((node.right, hd+1))
    
    for i in range(min_hd, max_hd+1):
        print(distance_map[i][-1], end=" ")


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
    bottom_view(root1)