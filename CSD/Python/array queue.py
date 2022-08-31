class Queue:
    def __init__(self,c):
        self.data=[]
        self.capacity=c
        self.front=0
        self.rear=0

    def __len__(self):
        return self.rear

    def isEmpty(self):
        return self.rear== self.front

    def isFull(self):
        return self.rear==self.capacity

    def enQueue(self,value):
        if self.isFull():
            print("Queue is full")
        else:
            self.data.append(value)
            self.rear+=1

    def deQueue(self):
        if self.isEmpty():
            print("Queue is empty")
        else:
            self.rear-=1
            return self.data.pop(self.front)

    def display(self):
        print()
        for i in range (self.front,self.rear):
            print(self.data[i],end="->")

    def first(self):
        if self.isEmpty():
            print("Queue is empty")
        else:
            return self.data[self.front]

