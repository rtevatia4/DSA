"""
                    1
                2       3
            4      6  7   8
        5                   9

o/p - 5 4 2 1 6 7 3 8 9

WE can use horizontal distance approach
"""


from collections import defaultdict
import collections
from Node import Node


def vertical_order_traversal(root, _distance_map, _x_distance):    # O(nlogn) as we are sorting the map later on
    if root is None:
        return root
    
    _distance_map[_x_distance].append(root.val)

    vertical_order_traversal(root.left, _distance_map, _x_distance-1)
    vertical_order_traversal(root.right, _distance_map, _x_distance+1)

def vertical_order_traversal_optimized(root):    # O(n)
    if root is None:
        return root
    distance_map = defaultdict(list)
    queue = collections.deque([(root,0)])
    min_d = 0
    max_d = 0
    while queue:
        node, hd = queue.popleft()
        min_d = min(min_d,hd)
        max_d = max(max_d,hd)
        distance_map[hd].append(node.val)
        if node.left:
            queue.append((node.left,hd-1))
        if node.right:
            queue.append((node.right,hd+1))
            
    for i in range(min_d,max_d+1):
        for items in distance_map[i]:
            print(items, end=" ")

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
    print("\nVertical Ordering from brute force O(nlogn) algorithm")
    distance_map = defaultdict(list)
    vertical_order_traversal(root1, distance_map, 0)
    for k in sorted(distance_map):
        for val in distance_map[k]:
            print(val, end= " ")
    
    print("\nVertical Ordering from optimized O(n) algorithm")
    vertical_order_traversal_optimized(root1)
