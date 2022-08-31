class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class Stack:
    def __init__(self):
        self.head=None

    def push(self,data):
        new=Node(data)
        if self.head==None:
            self.head=new
        else:
            temp=self.head
            while temp.next:
                temp=temp.next
            temp.next= new

    def display(self):
        temp=self.head
        while temp:
            if temp.next != None:
                print(temp.data,end=" ")
                temp=temp.next
            else:
                print(temp.data)
                temp=temp.next

    def pop(self):
        if self.check()==True:
            temp=self.head
            before=self.head
            if temp==None:
                self.head=None
                print("Pop successfully")
            else:
                while temp.next!=None:
                    before=temp
                    temp=temp.next
                before.next=None
                print("Pop successfully.")

    def top(self):
        if self.check()==True:
            temp=self.head
            if temp.next==None:
                print(temp.data)
            else:
                while temp.next!=None:
                    temp=temp.next
                print(temp.data)
    def check(self):
        if self.head==None:
            print("The stack is empty")
            return False
        else:
            return True






def menu():
    print("1-Push into stack")
    print("2-Pop the stack")
    print("3-Display the top value")
    print("4-Display the stack")
    print("5-Exit")
    while True:
        try:
            choice=int(input("Choose the function from the menu: "))
            if choice>0 and choice <=5:
                return choice
            else:
                print("Please choose the valid function from the menu.")
        except:
            print("Pleas enter a number.")

def enternum(s):
    try:
        n=int(input(s))
        return n
    except:
        print("Please enter a number.")



#main program:
s=Stack()
while True:
    pick=menu()
    if pick == 1:
        n=enternum("Please enter number you want to push into the stack: ")
        s.push(n)
    if pick ==2:
        s.pop()
    if pick ==3:
        s.top()
    if pick ==4:
        s.display()
    if pick ==5:
        exit()



