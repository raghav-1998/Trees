"""
Here, we are using 1st approach of finding diameter of Tree..

3 cases:
1. Diameter exist only in left subtree
2. Diameter exist only in right subtree
3. Diameter exist from left subtree to right subtree(height of LST + 1 + height of RST)

Final answer is maximum of 3..

T(N): O(N^2) where N is number of nodes
Space : O(Height)
"""

class Node:
    def __init__(self,key):
        self.left=None
        self.right=None
        self.data=key

class BinaryTree:
    def __init__(self):
        self.root=None

    def height(self,root):
        if(root==None):
            return 0
        
        left=self.height(root.left)
        right=self.height(root.right)

        return 1+max(left,right)

    def diameter(self,root):

        if(root == None):
            return 0
        
        #diameter exist only in left subtree
        op1=self.diameter(root.left)

        #diameter exist only in right subtree
        op2=self.diameter(root.right)

        #diameter from left subtree to right subtree
        op3=self.height(root.left)+self.height(root.right)+1

        return max(op1,max(op2,op3))


if __name__=="__main__":
    tree=BinaryTree()

    root=Node(1)
    root.left=Node(2)
    root.right=Node(3)
    root.left.left=Node(4)
    root.left.right=Node(5)
    root.right.left=Node(6)
    root.right.right=Node(7)

    tree.root=root

    print(tree.diameter(root))