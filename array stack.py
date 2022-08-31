class Arraystack:
    def __init__(self,c):
        self.capacity=c
        self.data=[]
        self.length=0

    def __len__(self):
        return self.length

    def Isempty(self):
        return self.length==0

    def display(self):
        if (self.length==0):
            print("Stack is empty")
        else:
            for i in self.data:
                print(i, end="->")

    def push(self,value):
        if self.length== self.capacity:
            print("Stack is full")
        else:
            self.data.append(value)
            self.length+=1

    def pop(self):
        if (self.Isempty()):
            print("Stack is empty")
        else:
            value= self.data.pop()
            self.length -=1
            return value

    def top(self):
        if (self.length==0):
            print("Stack is empty")
        else:
            return self.data[self.length-1]

s=Arraystack(4)
s.display()
print("Pop: ",s.pop())
s.push(1)
s.push(2)
s.push(3)
s.push(4)
s.display()
s.push(4)
print()
s.display()
print()
s.pop()
s.display()
print()
print(s.top())


