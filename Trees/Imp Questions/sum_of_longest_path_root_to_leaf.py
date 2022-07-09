"""
https://www.geeksforgeeks.org/sum-nodes-longest-path-root-leaf-node/
Given a binary tree containing n nodes. The problem is to find the sum of all nodes on the longest path
 from root to leaf node. If two or more paths compete for the longest path, 
 then the path having maximum sum of nodes is being considered.
 Input : Binary tree:
        4        
       / \       
      2   5      
     / \ / \     
    7  1 2  3    
      /
     6
Output : 13
"""

from Node import Node

def longest_path_sum(root, curr_sum, curr_len, max_sum, max_len):
    if not root:
        if curr_len > max_len[0]:
            max_len[0] = curr_len
            max_sum[0] = curr_sum
        elif curr_len == max_len[0]:
            max_sum[0] = max(curr_sum,max_sum[0])
        return None
    curr_sum += root.val
    longest_path_sum(root.left, curr_sum, curr_len+1, max_sum, max_len)
    longest_path_sum(root.right, curr_sum, curr_len+1, max_sum, max_len)
    return max_sum[0]
    
if __name__ == "__main__":
    root = Node(4)
    root.left = Node(2)
    root.right = Node(5)
    root.left.left = Node(7)
    root.left.right = Node(1)
    root.left.right.left = Node(6)
    root.right.left = Node(2)
    root.right.right = Node(3)

    max_sum = [-float("inf")]
    max_len = [0]
    print(longest_path_sum(root, 0, 0, max_sum, max_len))