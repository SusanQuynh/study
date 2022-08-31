import ctypes
import random
def menu():
    print("1-Generate an array.")
    print("2-Add a number to the last place in array.")
    print("3-Insert any number into array.")
    print("4-Delete by index.")
    print("5-Print the array.")
    print("6-Exit")
    while True:
        try:
            choice=int(input("Choose a function in the menu: "))
            if choice >0 and choice <7:
                return choice
            else:
                print("Please choose a function in the menu.")
        except:
            print("Please enter a number that exist in the menu.")

def getnum(s):
    try:
        n=int(input(s))
        if n>0:
            return n
        else:
            print("Please enter a positive number.")
    except:
        print("Please enter a number.")
class DynamicArray:
    def __init__(self):
        self._size=0
        self._capacity=1
        self._element=self._makeArray(self._capacity)

    def _makeArray(self,c):
        return (c * ctypes.py_object)()

    def showInfor(self):
        print("Size: ",self._len_())
        print("Capacity: ",self._capacity)
        for i in range(self._size):
            if i < self._size-1:
                print(" ",self._element[i],end=" ")
            else:
                print(" ", self._element[i])

    def _len_(self):
        return self._size

    def _reSize (self,c):
        b= self._makeArray(c)
        for i in range (self._size):
            b[i]=self._element[i]
        self._element=b
        self._capacity=c

    def append(self,obj):
        self._element[self._size]= obj
        self._size+=1
        if self._size == self._capacity:
            self._reSize(2*self._capacity)
    
    def insert(self,index,data):
        if self._size == self._capacity:
            self._reSize(2*self._capacity)
        for i in range (self._size,index,-1):
            self._element[i]= self._element[i-1]
        self._element[index]= data
        self._size+=1

    def deletByIndex(self, index):
        if index < self._size:
            for i in range (index,self._size-1):
                self._element[i]=self._element[i+1]
            self._element[self._size-1]=None
            self._size-=1

    def checkarray(self):
        if self._size==0:
            return False
        else:
            return True
#main program:
arr= DynamicArray()
while True:
    pick=menu()
    if pick == 1:
        n=getnum("Enter the size of the array: ")
        for i in range (n):
            arr.append(random.randint(0,10))
    if pick==2:
        n=getnum("Enter the number you want to add: ")
        arr.append(n)
    if pick==3:
        location=getnum("Enter where you want to insert: ")
        n=getnum("Enter number you want to insert: ")
        arr.insert(location,n)

