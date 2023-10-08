class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.lCount = 0
        self.theight = 0
    def insert(self, root, key):   #The worst-case time complexity of insert operations is O(h) where h is the height of the Binary Search Tree. 
        if not root:
            return Node(key)
        if key > root.val:
            root.right = self.insert(root.right, key)
        elif key < root.val:
            root.left = self.insert(root.left, key)
        return root
    
    def insertIterative(self, root, key):
        node = Node(key)
        if not root:
            root = node
            return root
        temp = root
        prev = None
        while temp != None:
            if temp.val > key:
                prev = temp
                temp = temp.left
            elif temp.val < key:
                prev = temp
                temp = temp.right
        if prev.val > key:
            prev.left = node
        else:
            prev.right = node
        return root

    def inorderTraversal(self, root):
        if not root:
            return root
        self.inorderTraversal(root.left)
        print(root.val, end=" ")
        self.inorderTraversal(root.right)
    
    def findMin(self, root):
        if not root:
            return -1
        curr = root
        while curr.left:
            curr = curr.left
        return curr.val

    def findMax(self, root):
        if not root:
            return -1
        curr = root
        while curr.right:
            curr = curr.right
        return curr.val

    def countLeaf(self, root):
        if not root.left and not root.right:
            self.lCount+=1
            print("root : ", root.val)
            print("count here is: ", self.lCount)
            return 
        
        # while root:
        print("left = ", root.left.val)
        print("right = ", root.right.val)
        if root.left:
            self.countLeaf(root.left)
        if root.right:
            self.countLeaf(root.right)

        return self.lCount

    def height(self, root):
        # if not root.left and not root.right:
        if not root:
            return -1
        # if not root.right and root.left:
        #     return self.height(root.left) + 1
        # if not root.left and root.right:
        #     return self.height(root.right) + 1
        self.theight = max(self.height(root.left), self.height(root.right)) + 1
        return self.theight

if __name__ == "__main__":
    """Let us create following BST
          50
       /     \
      30      70
     /  \    /  \
    20  40  60   80
    """
    root = None
    bst = BinarySearchTree()
    root = bst.insertIterative(root, 50)
    root = bst.insertIterative(root, 30)
    root = bst.insertIterative(root, 80)
    root = bst.insertIterative(root, 20)
    root = bst.insertIterative(root, 40)
    root = bst.insertIterative(root, 70)
    root = bst.insertIterative(root, 60)

    bst.inorderTraversal(root)
    # print("Min is:", bst.findMin(root))
    # print("Max is:", bst.findMax(root))
    # print("count : ", bst.countLeaf(root))
    print("height: ", bst.height(root))


