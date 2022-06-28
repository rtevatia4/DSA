"""
zig zag/spiral traversal is level order traversal where levels are explored in zig zag manner
"""
import collections
from Node import Node

def spiral_traversal(root):   # Time O(n), space O(n)
    if not root:
        return root
    queue = collections.deque()
    queue.append(root)
    ans = []
    direction=False
    while queue:
        temp = []
        for i in range(len(queue)):
            node = queue.popleft()
            temp.append(node.val)
            #print(node.val, end=" ")
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        if not direction:
            for item in temp:
                ans.append(item)
        else:
            for item in temp[::-1]:
                ans.append(item)
        direction = not direction
    return ans
            
            

if __name__== "__main__":
    root1 = Node(1)
    root1.left = Node(2)
    root1.right = Node(3)
    root1.left.left = Node(4)
    root1.left.left.left = Node(5)
    root1.left.left.right = Node(9)
    root1.left.right = Node(6)
    root1.right.left = Node(7)
    root1.right.right = Node(8)
    """
                        1
                2              3
            4       6       7       8
        5      9
    """
    print(spiral_traversal(root1))