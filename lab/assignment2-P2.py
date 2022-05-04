studentlist = list()
number=0
def menu():
    print("1-Enter number of student in the class")
    print("2-Add student list")
    print("3-Remove student with the same name")
    print("4-Print out student whose first name contain the string an ")
    print("5-Print the list in descending order")
    print("6-Quit")

    while True:
        try:
            choice= int(input("Choose a function from the menu: "))
            if 0<choice and choice<7:
                break
            else:
                print("Please choose a function from the menu")

        except:
            print("Please enter a number")
    return choice

def enternum():
    while True:
        try:
            n=int(input("Enter a number: "))
            if 10<n and n <=100:
                return n
            else:
                print("Please enter a number from 10 to 100")
        except:
            print("Please enter a number.")

def entername():
    while True:
        try:
            name=input("Enter name: ")
            name.capitalize()
            if len(name)<1 and name== ' ':
                print("Please enter a valid name.")
            else:
                break
        except:
            print("Please enter a valid name.")
    return name

def addstudentlist(number):
    num=number
    for i in range (0,num):
        name=entername()
        studentlist.append(name)
    return studentlist

def removestudensamename():
    i=0
    while i<len(studentlist):
        name= studentlist[i]
        count=studentlist.count(name)
        if count==1:
            i+=1
        else:
            studentlist.remove(name)
    return studentlist

def firstnamcontainstring():
    string='an'
    studentlist1=list()
    for name in studentlist:
        if string in name:
            studentlist1.append(name)
    return studentlist1

def descendingorder():
    studentlist.sort(reverse=True)
    return studentlist

def checklist():
    res=True
    if len(studentlist)<1:
        res=False
    return res

#chuong trinh chinh:
while True:
    select=menu()
    if select==1:
        number=enternum()
    if select==2:
        studentlist=addstudentlist(number)
    if select==3:
        if checklist():
            studentlist = removestudensamename()
        else:
            print("There doesn't have any list here")
    if select==4:
        if checklist():
            print(firstnamcontainstring())
        else:
            print("There doesn't have any list here")
    if select==5:
        if checklist():
            print(descendingorder())
        else:
            print("There doesn't have any list here")
    if select==6:
        exit()
