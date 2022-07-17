

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

    print(tree.height(root))




