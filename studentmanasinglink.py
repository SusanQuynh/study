class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class Student:
    def __init__(self,id,name,address,mark):
        self.id=id
        self.name=name
        self.address=address
        self.mark=mark

class StudentManagement:
    def __init__(self):
        self.head=None

    def insertandsort(self,data):
        new=Node(data)
        if self.head==None:
            self.head=new
            return
        else:
            p=self.head
            if data.mark< p.data.mark:
                new.next=p
                self.head=new
            else:
                while p.next and data.mark>p.data.mark:
                    p=p.next
                if p.next is not None:
                    new.next=p.next
                    p.next-new
                else:
                    p.next=new

    def insert(self,data):
        new=Node(data)
        if self.head==None:
            self.head=new
        else:
            p=self.head
            while p.next:
                p=p.next
            p.next = new


    def delete(self,id):
        if self.head==None:
            print("Empty")
        else:
            p=self.head
            pr=self.head
            while p:
                if p.data.id==id:
                    x=p
                    pr.next=p.next
                    x.next=None
                pr=p
                p=p.next

    def showInfo(self):
        if self.head==None:
            print("Empty")
        else:
            p=self.head
            while p:
                print(p.data.id,p.data.name,p.data.address,p.data.mark)
                p=p.next

    def search(self,name):
        if self.head==None:
            print("Empty")
        else:
            p=self.head
            while p:
                if name in p.data.name:
                    print(p.data.id,p.data.name,p.data.address,p.data.mark)
                p=p.next

    def sort(self):
        p=self.head
        while p:
            after=p
            while after:
                if p.data.mark > after.data.mark:
                    temp=after.data
                    after.data=p.data
                    p.data=temp
                after=after.next
            p = p.next


def inputinfo(s):
    try:
        n=input(s)
        if len(n)<1 or n==" ":
            print("Please enter something")
        else:
            return n
    except:
        print("Please enter info")

def inputnum(s):
    try:
        n=int(input(s))
        if n<0:
            print("Please enter positive number.")
        else:
            return n
    except:
        print("Please enter a number.")

st=StudentManagement()
s1=Student("1","Minh Đăng","3",4)
st.insert(s1)
st.showInfo()
s2=Student("2","Hà Lê","1",10)
st.insert(s2)
st.showInfo()
s3=Student("3","Quynh","5",8)
st.insert(s3)
st.showInfo()
print()
st.sort()
st.showInfo()





