class Node:
    def __init__(self,data,key):
        self.data=data
        self.key=key
        self.left=None
        self.right=None
class BinaryTree:
    def __init__(self,node):
        self.root=node

    def height(self,root):
        if root is None:
            return 0
        lheight=self.height(root.left)
        rheight=self.height(root.right)
        if lheight > rheight:
            return lheight+1
        return rheight+1

    def Printallnodesamelevel(self,root,level):
        if root is None:
            return
        if level==1:
            print(root.data,end=" ")
        elif level>1:
            self.Printallnodesamelevel(root.left,level-1)
            self.Printallnodesamelevel(root.right,level-1)

    def printallNode(self):
        h=self.height(self.root)
        self.Printallnodesamelevel(self.root,3)
        print()
        for i in range (1,h+1):
            self.Printallnodesamelevel(self.root,i)

    def prinAllNodeBFT_Queue(self):
        if self.root is None:
            return
        q=[]
        q.append(self.root)
        while len(q)>0:
            print(q[0].data,end=" ")
            node=q.pop(0)
            if node.left is None:
                q.append(node.left)
            if node.right is None:
                q.append(node.right)

    def printInorder(self,root):
        if root:
            self.printInorder(root.left)
            print(root.data,end=" ")
            self.printInorder(root.right)

    def printPreorder(self,root):
        if root:
            print(root.data, end=" ")
            self.printPreorder(root.left)
            self.printPreorder(root.right)

    def printPostorder(self,root):
        if root:
            self.printPostorder(root.left)
            self.printPostorder(root.right)
            print(root.data,end=" ")

def menu():
    print("1-Insert the information.")
    print("2-Print the height of the tree.")
    print("3-Print all the node the same level.")


#main:
BTree=BinaryTree(Node("A"))
BTree.root.left=Node("B")
BTree.root.right=Node("C")
BTree.root.left.left=Node("D")
BTree.root.right.left=Node("F")
BTree.root.left.right=Node("E")
BTree.root.right.right=Node("G")
BTree.root.left.right.left=Node("H")
BTree.root.left.right.right=Node("I")
print(BTree.height(BTree.root))
BTree.printallNode()
print()
print("Queue")
print(BTree.prinAllNodeBFT_Queue())
BTree.printInorder(BTree.root)
print()
BTree.printPostorder(BTree.root)
print()
BTree.printPreorder(BTree.root)

