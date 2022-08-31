
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class Linkedlist:
    def __init__(self):
        self.head=None
    
    def printList(self):
        print("--------------------------")
        temp=self.head
        while temp:
            print(temp.data,end=" ")
            temp=temp.next
        print("")

    def search(self,value):
        temp=self.head
        count=1
        while temp:
            if temp.data==value:
                return count
            count+=1
            temp=temp.next
        return count

    def insertFirst(self,data):
        newNode= Node(data)
        newNode.next=self.head
        self.head=newNode


    def insertafter(self,value,data):
        temp=self.head
        while temp:
            if temp.data == value:
                newNode=Node(data)
                newNode.next=temp.next
                temp.next=newNode
                break
            temp=temp.next

    def insertlast(self,data):
        newNode=Node(data)
        temp=self.head
        while temp.next:
            temp=temp.next
        temp.next=newNode
    
    def deletefirst(self):
        self.head=self.head.next
    
    def deleteafter(self,value):
        temp=self.head
        while temp:
            if temp.data==value:
                temp.next=temp.next.next
                return 
            temp=temp.next 
#main program:
llist=Linkedlist()
llist.insertFirst(1)
llist.printList()
llist.insertFirst(2)
llist.printList()
llist.insertafter(1,3)
llist.printList()
llist.insertlast(4)
llist.printList()
llist.deletefirst()
llist.printList()
llist.deleteafter(3)
llist.printList()