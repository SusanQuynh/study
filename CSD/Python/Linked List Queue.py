class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class LinkedListQueue:
    def __init__(self):
        self.head = None
    def isempty(self):
        return self.head is None
    def printqueue(self):
        if self.isempty():
            print("Queue is empty")
        else:
            p = self.head
            print("Here is your current queue: ", end="")
            while p:
                print(p.data, end=" -> ")
                p = p.next
            print()
    def enqueue(self, data):
        if self.isempty():
            self.head = Node(data)
        else:
            new = Node(data)
            p = self.head
            while p.next:
                p = p.next
            p.next = new
    def dequeue(self):
        if self.isempty():
            print("Queue is empty")
        else:
            pop = self.head
            self.head = self.head.next
            pop.next = None
            return pop.data
    def first(self):
        if self.isempty():
            print("Queue is empty")
        else:
            return self.head.data
    def len(self):
        count = 0
        p = self.head
        while p:
            count += 1
            p = p.next
        return count

llq = LinkedListQueue()
llq.enqueue(4)
llq.enqueue(3)
llq.enqueue(2)
llq.enqueue(1)
llq.printqueue()
print("First element of queue:", llq.first())
print("Length of queue:", llq.len())
llq.dequeue()
llq.printqueue()
