"""
Convert a Binary Search Tree to a sorted Circular Doubly-Linked List in place.

You can think of the left and right pointers as synonymous to the predecessor and successor pointers in a doubly-linked list. For a circular doubly linked list, the predecessor of the first element is the last element, and the successor of the last element is the first element.

We want to do the transformation in place. After the transformation, the left pointer of the tree node should point to its predecessor, and the right pointer should point to its successor. You should return the pointer to the smallest element of the linked list.
https://leetcode.com/problems/convert-binary-search-tree-to-sorted-doubly-linked-list/description/

"""

# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


import collections
from typing import Optional


class Solution:
    def treeToDoublyList(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return root
        q=collections.deque()

        def inOrder(node):
            if not node:
                return
            inOrder(node.left)
            q.append(node)
            inOrder(node.right)
        inOrder(root)
        
        prev = q.popleft()
        prev.left = None
        prev.right = None
        root = prev
        while q:
            node = q.popleft()
            node.right = None
            node.left = prev
            prev.right = node
            prev = node
        
        prev.right = root
        root.left = prev
        return root



        