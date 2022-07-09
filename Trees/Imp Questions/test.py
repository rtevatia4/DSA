"""
https://www.geeksforgeeks.org/print-k-sum-paths-binary-tree/

A binary tree and a number k are given. Print every path in the tree with sum of the nodes in the path as k. 
A path can start from any node and end at any node and must be downward only, i.e. 
they need not be root node and leaf node; 
and negative numbers can also be there in the tree.

Input : k = 5  
        Root of below binary tree:
           1
        /     \
      3        -1
    /   \     /   \
   2     1   4     5                        
        /   / \     \                    
       1   1   2     6    
                       
Output :
3 2 
3 1 1 
1 3 1 
4 1 
1 -1 4 1 
-1 4 2 
5 
1 -1 5 
"""
from Node import Node

def path(root, k):
    count = 0
    path = []
    def k_sum_path(root, path, k, count):
        if root is None:
            return None
        
        path.append(root.val)
        
        k_sum_path(root.left, path, k, count)
        k_sum_path(root.right, path, k, count)

        path_sum = 0
        for i in range(len(path)-1,-1,-1):
            path_sum += path[i]
            if path_sum == k:
                print(path[i:])
                count +=1
        
        path.pop(-1)
        print(count)
    k_sum_path(root, path, k, count)
    #print(count)

# Driver Code
if __name__ == '__main__':
 
    root = Node(1)
    root.left = Node(3)
    root.left.left = Node(2)
    root.left.right = Node(1)
    root.left.right.left = Node(1)
    root.right = Node(-1)
    root.right.left = Node(4)
    root.right.left.left = Node(1)
    root.right.left.right = Node(2)
    root.right.right = Node(5)
    root.right.right.right = Node(2)
 
    
    k = 5
    path(root, k)
    #print("Total number of paths are: ", count[0])