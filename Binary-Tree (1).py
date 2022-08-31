class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self, node):
        self.root = node
    
    def height(self, root):
        if root is None:
            return 0
        lheight = self.height(root.left)
        rheight = self.height(root.right)
        if lheight > rheight:
            return lheight + 1
        return rheight + 1
    def printAllnodesamelevel(self, root, level):
        if root is None:
            return
        if level == 1:
            print(root.data, end=" ")
        elif level > 1:
            self.printAllnodesamelevel(root.left, level - 1)
            self.printAllnodesamelevel(root.right, level - 1)
    def printAllNode(self):
        h = self.height(self.root)
        for i in range(1, h+1):
            self.printAllnodesamelevel(self.root, i)
    def printAllnodes_Queue(self):
        if self.root is None:
            return
        n = []
        n.append(self.root)
        while len(n) > 0:
            print(n[0].data, end=" ")
            node = n.pop(0)
            if node.left is not None:
                n.append(node.left)
            if node.right is not None:
                n.append(node.right)
    def printAllnode_Inorder(self, root):
        if root:
            self.printAllnode_Inorder(root.left)
            print(root.data, end=" ")
            self.printAllnode_Inorder(root.right)
    def printAllnode_Postorder(self, root):
        if root:
            self.printAllnode_Postorder(root.left)
            self.printAllnode_Postorder(root.right)
            print(root.data, end=" ")
    def printAllnode_Preorder(self, root):
        if root:
            print(root.data, end=" ")
            self.printAllnode_Preorder(root.left)
            self.printAllnode_Preorder(root.right)
btree = BinaryTree(Node("A"))
btree.root.left = Node("B")
btree.root.right = Node("C")
btree.root.left.left = Node("D")
btree.root.left.right = Node("E")
btree.root.right.left = Node("F")
btree.root.right.right = Node("G")
btree.root.left.right.left = Node("H")
btree.root.left.right.right = Node("I")
print("Height of tree:", btree.height(btree.root))
print(btree.printAllnodesamelevel(btree.root, 2))
btree.printAllNode()
print("\n ------------")
btree.printAllnodes_Queue()
print("\n ------------")
btree.printAllnode_Inorder(btree.root)
print("\n ------------")
btree.printAllnode_Postorder(btree.root)
print("\n ------------")
btree.printAllnode_Preorder(btree.root)