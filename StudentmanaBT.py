# Viết chương trình quản lý học sinh.
#1. Xây dựng menu:
#2. Xây dựng cấu trúc: Node, Student, Binary.
#3.Insert
#4. update (Key,view value)
#5. Search (Key) -> Show information.
#6. Delete
#7. Show information

class Node():
    def __init__(self,key,value):
        self.value=value
        self.key=key
        self.left=None
        self.right=None
class Student():
    def __init__(self,ID,name,mark):
        self.ID=ID
        self.name=name
        self.mark=mark

class BinaryTree():
    def __init__(self,node):
        self.root= node

    def insert(self,root,key,value):
        new = Node(key, value)
        if root is None:
            root = new
            return root
        else:
            if root.key == key:
                return root
            elif root.key > key:
                root.left= self.insert(root.left,key,value)
            else:
                root.right=self.insert(root.right,key,value)
            return root

    def show_infor(self,root):
        if root:
            self.show_infor(root.left)
            print(root.value.ID, "|", root.value.name, "|", root.value.mark)
            self.show_infor(root.right)

    def search(self,root,key):
        if root is None:
            print("ID not available")
            return root
        else:
            if root.key == key:
                return root
            if root.key < key:
                return self.search(root.right, key)
            return self.search(root.left, key)

    def minvalue(self,root):
        if root is None:
            return root
        current=root
        while current.left is not None:
            current=current.left
        return current

    def deletion(self,root,key):
        delete= self.search(root,key)
        if delete is None:
            return delete
        else:
            if delete.left is None:
                temp=delete.right
                delete=None
                return temp
            elif delete.right is None:
                temp=delete.left
                delete=None
                return temp
            temp=self.minvalue(delete.right)
            delete.key = temp.key
            delete.value = temp.value
            delete.right=self.deletion(delete.right,temp.key)
            print("Done!!!")


    def update(self,root,key,name,mark):
        up=self.search(root,key)
        if up is not None:
            up.value.name=name
            up.value.mark=mark
            print("Update successfully.")
def menu():
    print("1:Insert new student.")
    print("2:Search for a student.")
    print("3:Update student information.")
    print("4:Delete student information.")
    print("5:Show student information.")
    print("6:Exit.")
    while True:
        try:
            choice=int(input("Choose a function from the menu: "))
            if choice <1 or choice >6:
                print("Choose function again.")
            else:
                return choice
        except:
            print("Enter a number.")
def getID(s):
    try:
        n=int(input(s))
        if n<0:
            print("Please enter a positive number.")
        else:
            return n
    except:
        print("Please enter a number.")

def getname(s):
    n=input(s)
    if len(n)<0 or n == ' ':
        print("Please enter a name.")
    else:
        return n

def getmark(s):
    try:
        n=float(input(s))
        if n<0 or n>10:
            print("Please enter a number from 0 to 10.")
        else:
            return n
    except:
        print("Please enter a number.")




#main program:
bst=None
while True:
    pick=menu()
    if pick == 1:
        id = getID("Enter student's ID: ")
        name = getname("Enter student's name: ")
        mark = getmark("Enter student's mark: ")
        student = Student(id,name,mark)
        if bst is None:
            bst = BinaryTree(Node(id,student))
        else:
            bst.insert(bst.root,id,student)
    else:
        if pick == 6:
            exit()
        elif bst is not None:
            if pick == 2:
                id = getID("Enter student's ID you want to find: ")
                data = bst.search(bst.root,id)
                if data is not None:
                    print("The ID was found.")
                    print("Student's ID: ",data.value.id)
                    print("Student's name: ",data.value.name)
                    print("Student's mark: ",data.value.mark)
            if pick == 3:
                id = getID("Enter student's ID you want to update: ")
                data=bst.search(bst.root,id)
                if data is not None:
                    print("The ID was found.")
                    name = getname("Enter student's name you want to update: ")
                    mark = getmark("Enter student's mark you want to update: ")
                    bst.update(bst.root,id,name,mark)
            if pick == 4:
                id = getID("Enter student's ID you want to delete: ")
                do = bst.search(bst.root,id)
                if do is not None:
                    print("The ID was found.")
                    bst.deletion(bst.root,id)
            if pick == 5:
                bst.show_infor(bst.root)
        else:
            print("The list is empty")


