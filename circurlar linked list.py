class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class CircurlarLinkedList:
    def __init__(self):
        self.last=None

    def addToEmty(self,data):
        if self.last != None:
            return self.last
        temp=Node(data)
        self.last=temp
        self.last.next=self.last
        return self.last

    def addFirst(self,data):
        if self.last==None:
            return self.addToEmty(data)
        temp=Node(data)
        temp.next=self.last.next
        self.last.next=temp
        return self.last

    def addEnd(self,data):
        if self.last==None:
            return self.addToEmty()
        temp =Node(data)
        temp.next=self.last.next
        self.last.next=temp
        self.last=temp
        return self.last

    def addafter(self,value,data):
        if self.last==None:
            return None
        temp=Node(data)
        p=self.last.next
        while p:
            if(p.data==value):
                temp.next=p.next
                p.next=temp
                if p==self.last:
                    self.last=temp
                    return self.last
                else:
                    return self.last
            p=p.next
            if p== self.last.next:
                print("Cannot find the value.")
                break
    def printList(self):
        print("---------------------------")
        if self.last==None:
            print("List is empty.")
            return
        temp=self.last.next
        while temp:
            print(temp.data,end=" ")
            temp=temp.next
            if temp== self.last.next:
                break
        print(" ")

    def deleteFirst(self):
        if self.last==None:
            print("There is nothing to delete")
            return
        self.last.next=self.last.next.next

    def deletelast(self):
        if self.last is None:
            print("List is empty")
            return
        temp = self.last.next
        prev = self.last.next
        while temp:
            if temp == self.last:
                prev.next = self.last.next
                prev = self.last
                return self.last
            prev = temp
            temp = temp.next

    def deletebyvalue(self, value):
        if self.last is None:
            print("List is empty")
            return
        temp = self.last.next
        if temp.data == value:
            self.deleteFirst()
            return
        prev = self.last.next
        while temp:
            if temp.data == value:
                if temp == self.last:
                    self.deletelast()
                    return self.last
                else:
                    prev.next = temp.next
                    return
            prev = temp
            temp = temp.next


#main program:
cl= CircurlarLinkedList()
last=cl.addToEmty(1)
cl.printList()
last=cl.addFirst(2)
cl.printList()
last=cl.addEnd(3)
cl.printList()
last=cl.addEnd(4)
cl.printList()
last=cl.addafter(3,0)
cl.printList()
print("After delete: ")
last=cl.deleteFirst()
cl.printList()
last=cl.deletelast()
cl.printList()
last=cl.deletebyvalue(3)
cl.printList()