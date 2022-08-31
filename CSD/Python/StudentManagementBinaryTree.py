class Node:
    def __init__(self, key, value):
        self.value = value
        self.key = key
        self.left = None
        self.right = None

class Student:
    def __init__(self, id, name, mark):
        self.id = id
        self.name = name
        self.mark = mark

class StudentManagement:
    def __init__(self, node):
        self.root = node
    
    def insert(self, root, key, value):
        new = Node(key, value)
        if root is None:
            root = new
            return root
        else:
            if root.key == key:
                print("ID is already taken") 
                return root
            elif root.key > key:
                root.left = self.insert(root.left, key, value)
            else:
                root.right = self.insert(root.right, key, value)
            return root
    
    def show_infor(self, root):
        if root is not None:
            self.show_infor(root.left)
            print(root.value.id, "|", root.value.name, "|", root.value.mark)
            self.show_infor(root.right)
    
    def search(self, root, key):
        if root is None:
            print("ID not available")
            return root
        else:
            if root.key == key:
                print("The ID was found.")
                return root
            if root.key < key:
                return self.search(root.right, key)
            return self.search(root.left, key)
    
    def minNode(self, root):
        current = root
        while current.left:
            current = current.left
        return current
    
    def delete(self, root, key):
        if key < root.key:
            root.left = self.delete(root.left, key)
        elif key > root.key:
            root.right = self.delete(root.right, key)
        else:
            if root.left is None:
                temp = root.right
                root = None
                return temp
            elif root.right is None:
                temp = root.left
                root = None
                return temp
            temp = self.minNode(root.right)
            root.key = temp.key
            root.value = temp.value
            root.right = self.delete(root.right, temp.key)
        return root
                
    def update(self, root, key, newvalue):
        if root is None:
            return root
        else:
            if root.key > key:
                root.left = self.update(root.left, key, newvalue)
            elif root.key < key:
                root.right = self.update(root.right, key, newvalue)
            else:
                root.value = newvalue
            return root
    
def menu():
    print("----------------------------------------")
    print("1: Insert new student")
    print("2: Search for a student by ID")
    print("3: Delete a student by ID")
    print("4: Update a student by ID")
    print("5: Show all student(s)")
    print("6: Quit")
    while True:
        try:
            choice = int(input("Select function: "))
            if choice > 0 and choice < 7:
                return choice
            else:
                print("Invalid function")
        except:
            print("Input must be an integer")

def getID(s):
    while True:
        try:
            id = int(input(s))
            if id > 0:
                return id
            else:
                print("ID must be positive")
        except:
            print("ID must be an integer")

def getname(s):
    while True:
        name = input(s)
        if name.isalpha():
            return name.title()
        else:
            print("Cannot leave blank")

def getmark(s):
    while True:
        try:
            mark = float(input(s))
            if mark < 0 or mark > 10:
                print("Mark must be between 0 and 10")
            else:
                return mark
        except:
            print("Mark must be a real number")

bst = None
while True:
    selection = menu()
    if selection == 1:
        id = getID("Enter student id: ")
        name = getname("Enter student name: ")
        mark = getmark("Enter student mark: ")
        student = Student(id, name, mark)
        if bst is None:
            bst = StudentManagement(Node(id, student))
        else:
            bst.insert(bst.root, id, student)
    else:
        if selection == 6:
            print("Goodbye")
            quit()
        elif bst is not None:        
            if selection == 2:
                id = getID("Enter ID of student: ")
                student = bst.search(bst.root, id)
                if student is not None:
                    print(student.value.id, "|", student.value.name, "|", student.value.mark)
            elif selection == 3:
                id = getID("Enter student you want to delete: ")
                if bst.search(bst.root, id) is not None:
                    bst.delete(bst.root, id)
            elif selection == 4:
                id = getID("Enter ID: ")
                if bst.search(bst.root, id) is not None:
                    newname = getname("Enter new student name: ")
                    newmark = getmark("Enter new student mark: ")
                    newstudent = Student(id, newname, newmark)
                    bst.update(bst.root, id, newstudent)
            else:
                bst.show_infor(bst.root)
        else:
            print("List is empty")     