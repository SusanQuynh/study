class Node:
    def __init__(self, data):
        self.next = None
        self.prev = None
        self.data = data


class DoublyLinkedList:
    def __init__(self):
        self.head = None
    
    def insertfirst(self, data):
        new = Node(data)
        new.next = self.head
        if self.head is not None:
            self.head.prev = new
        self.head = new
        return
    
    def insertlast(self, data):
        new = Node(data)
        if self.head is None:
            new = self.head
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        new.prev = temp
        temp.next = new
        return
    
    def insertbefore(self, value, data):
        if self.head is None:
            print("List is empty")
            return
        new = Node(data)
        temp = self.head
        while temp:
            if temp.data == value:
                if temp == self.head:
                    self.insertfirst(data)
                    return
                new.next = temp
                new.prev = temp.prev
                temp.prev.next = new
                temp.prev = new
                return
            temp = temp.next
        print("Value not available")
    
    def insertafter(self, value, data):
        if self.head is None:
            print("List is empty")
            return
        new = Node(data)
        temp = self.head
        while temp:
            if temp.data == value:
                if temp.next is None:
                    self.insertlast(data)
                    return
                new.next = temp.next
                new.prev = temp
                temp.next.prev = new
                temp.next = new
                return
            temp = temp.next
        print("Value not available")
    
    def deletefirst(self):
        if self.head is None:
            print("List is empty")
            return
        if self.head.next is None:
            self.head = None
            return
        self.head = self.head.next
        return
    
    def deletelast(self):
        if self.head is None:
            print("List is empty")
            return
        if self.head.next is None:
            self.head = None
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.prev.next = None
        return
    def deletebefore(self, value):
        if self.head is None:
            print("List is empty")
            return
        temp = self.head
        while temp:
            if temp.data == value:
                if temp == self.head:
                    print("No value is before this value")
                    return
                if temp.prev == self.head:
                    self.deletefirst()
                    return
                temp.prev.prev.next = temp
                temp.prev = temp.prev.prev
                return
            temp = temp.next
        print("Value not available")
    
    def deleteafter(self, value):
        if self.head is None:
            print("List is empty")
            return
        temp = self.head
        while temp:
            if temp.data == value:
                if temp.next is None:
                    print("No value is after this value")
                    return
                if temp.next.next is None:
                    self.deletelast()
                    return
                temp.next.next.prev = temp
                temp.next = temp.next.next
                return
            temp = temp.next
        print("Value not available")
    
    def printlist(self):
        if self.head is None:
            print("List is empty")
            return
        temp = self.head
        print("Here is current list: ", end="")
        while temp:
            print(temp.data, end=" ")
            temp = temp.next
        print()


def menu():
    print("_______________________________________")
    print("1-Add to the beginning of the list")
    print("2-Add to the bottom of the list")
    print("3-Add before a value in the list")
    print("4-Add after a value in the list")
    print("5-Delete the first value of the list")
    print("6-Delete the last value of the list")
    print("7-Delete a value before a given value")
    print("8-Delete a value after a given value")
    print("9-Show current list")
    print("10-Quit")
    while True:
        try:
            choice = int(input("Select function: "))
            if choice > 0 and choice < 11:
                return choice
            else:
                print("Function not available")
        except:
            print("Input must be an integer")

def getnum(s):
    while True:
        try:
            n = float(input(s))
            if int(n) == n:
                return int(n)
            return n
        except:
            print("Input must be a number")


dll = DoublyLinkedList()
while True:
    selection = menu()
    if selection == 1:
        addnum = getnum("Enter the value you want to add: ")
        dll.insertfirst(addnum)
    elif selection == 2:
        addnum = getnum("Enter the value you want to add: ")
        dll.insertlast(addnum)
    elif selection == 3:
        addnum = getnum("Enter the value you want to add: ")
        addpos = getnum("Before which value: ")
        dll.insertbefore(addpos, addnum)
    elif selection == 4:
        addnum = getnum("Enter the value you want to add: ")
        addpos = getnum("After which value: ")
        dll.insertafter(addpos, addnum)
    elif selection == 5:
        dll.deletefirst()
    elif selection == 6:
        dll.deletelast()
    elif selection == 7:
        delpos = getnum("Delete before which value: ")
        dll.deletebefore(delpos)
    elif selection == 8:
        delpos = getnum("Delete after which value: ")
        dll.deleteafter(delpos)
    elif selection == 9:
        dll.printlist()
    else:
        print("Have a nice day")
        quit()
