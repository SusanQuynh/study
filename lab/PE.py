studentlist=[[]]
def menu():
    while True:
        print("1-Enter information of 5 students.")
        print("2-Print information about students with the highest GPA")
        print("3-Print the list of student in descending order of GPA.")
        print("4-Remove student based on user id input.")
        print("5-Exit")

        while True:
            try:
                choice=int(input("Choose a function from the menu: "))
                if choice>0 and choice<6:
                    return choice
                else:
                    print("Please choose a function from the menu.")
            except:
                print("Please enter a number.")

def enterID(s):
    while True:
        try:
            n = input(s)
            if len(n)<1 or n==' ':
                print("Please enter valid ID.")
            else:
                if n[:2].isalpha() and n[2:].isdigit():
                    return n
                else:
                    print("Please enter valid information.")
        except:
            print("Please enter valid infomation.")
def entername(s):
    while True:
        try:
            n=input(s)
            if len(n)<1 or n==' ':
                print("Please enter a name.")
            elif n.isalpha():
                return n
            else:
                print("Please enter a name.")
        except:
            print("Please enter a valid name.")
def entergender(s):
    while True:
        try:
            n=input(s)
            if len(n)<1 or n==' ':
                print("Please enter a gender.")
            else:
                if n=='female' or n=='male' or n=='other':
                    return n
                else:
                    print("Please enter a gender.")
        except:
            print("Please enter a gender.")
def enternum(s):
    while True:
        try:
            n = int(input(s))
            if n > 0:
                return n
            else:
                print("Please enter a positive number.")
        except:
            print("Please enter a number.")

def entergrade(s):
    while True:
        try:
            n = int(input(s))
            if n <0 or n>10:
                print("Please enter a number in range (0,10).")
            else:
                return n
        except:
            print("Please enter a number.")

def enterstuinfo():
    id=enterID("Enter student's ID: ")
    id.lower()
    name=entername("Enter student's name: ")
    name.capitalize()
    gender = entergender("Enter gender: ")
    age= enternum("Enter student's age: ")
    mathgrade= entergrade("Enter math grade: ")
    physicsgrade=entergrade("Enter physic grade: ")
    chemistrygrade=entergrade("Enter chemistry grade: ")
    GPA=(mathgrade+physicsgrade+chemistrygrade)/3
    return [id,name,gender,age,mathgrade,physicsgrade,chemistrygrade,GPA]
def putstuinfointolist():
    for i in range(0,5):
        studentlist[i]=enterstuinfo()
def findhighestGPA():
    highestGPAlist=[]
    max=studentlist[0][7]
    id=0
    find=0
    for i in range(0,5):
        if int(studentlist[i][7])>=max:
            max=studentlist[i][7]
    for i in range (0,5):
        if int(studentlist[i][7])==max:
             highestGPAlist.append (i)
    return highestGPAlist

def printstuinfohighestGPA():
    for n in findhighestGPA():
        print("Student's information has the highest GPA")
        print("Student's ID: ",studentlist[n][0])
        print("Student's name: ", studentlist[n][1])
        print("Student's gender: ", studentlist[n][2])
        print("Studen's age: ",studentlist[n][3])
        print("Student's math grade: ", studentlist[n][4])
        print("Student's physics grade: ", studentlist[n][5])
        print("Student's chemistry grade: ", studentlist[n][6])
        print("Student's GPA: ", studentlist[n][7])
def sorter(item):
    return item[7]
def studentlistsort():
    studentlist1=list()
    studentlist1=sorted(studentlist,key=sorter,reverse=True)
    for i in range(0,5):
        print("===============")
        print("The ", i + 1, " student")
        print("Staff's ID: ", studentlist1[i][0])
        print("Staff's name: ", studentlist1[i][1])
        print("Staff's gender: ", studentlist1[i][2])
        print("Studen's age: ", studentlist1[i][3])
        print("Student's math grade: ", studentlist1[i][4])
        print("Student's physics grade: ", studentlist1[i][5])
        print("Student's chemistry grade: ", studentlist1[i][6])
        print("Student's GPA: ", studentlist1[i][7])

def removestudentbaseonid():
    id = enterID("Enter student's  ID want to remove: ")
    id.lower()
    remove=0
    check=0
    for i in range(0,5):
        if id == studentlist[i][0]:
            remove=i
            check=1
    if check==1:
        studentlist.pop(remove)
        print("Remove successfully.")
    else:
        print("ID didn't in the list")
#main program
while True:
    select=menu()
    if select==1:
        studentlist*=5
        putstuinfointolist()
    if select==2:
        printstuinfohighestGPA()
    if select==3:
        studentlistsort()
    if select==4:
        removestudentbaseonid()
    if select==5:
        exit()