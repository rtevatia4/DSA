"""
Bottom view of the binary tree
                        1
                2              3
            4       6       7       8
        5                              9

o/p - 1 2 4 5

Will use multiple approaches here.
Can use the preorder approach and use the level count to print left view.
Or can use BFS traversal and print only the first node of each level
"""

import collections
from Node import Node

def left_view_approach1_using_dictionary_in_preorder(root, level,d): # storing first element of each level
    if root is None:
        return

    if level not in d:
        d[level] = root.val
    left_view_approach1_using_dictionary_in_preorder(root.left, level+1,d)
    left_view_approach1_using_dictionary_in_preorder(root.right, level+1,d)
    return d

def left_view_using_BFS(root):
    if not root:
        return root
    queue = collections.deque([root])
    while queue:
        for i in range(len(queue)):
            node = queue.popleft()
            if i==0:
                print(node.val, end= " ")
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

def left_view_approach3_using_preorder(root, level, last_max_level): # printing first element of each element , and finding it while iterating using preorder traversal
    if root is None:
        return

    if last_max_level[0] < level:
        print(root.val, end=" ")
        last_max_level[0] = level

    left_view_approach3_using_preorder(root.left, level+1,last_max_level)
    left_view_approach3_using_preorder(root.right, level+1,last_max_level)

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
    print("\Approach 1 Using dictionary with preorder to store first node of each level")
    print(left_view_approach1_using_dictionary_in_preorder(root1,0,{}))
    print("\nApproach 2 BFS Approach")
    left_view_using_BFS(root1)
    print("\nApproach 3 - Using Preorder traversal with finding first node of each level(no additional memory")
    
    left_view_approach3_using_preorder(root1,1,[0])