numberlist=list()
def menu():
    print("1-Enter the list of integer.")
    print("2-Search for a value in a list.")
    print("3-Print the element with the largest value in the list.")
    print("4-Remove the element whose value is equal.")
    print("5-Print the list in ascending order")
    print("6-Quit")

    while True:
        try:
            choice=int(input("Choose a function from the menu: "))
            if choice>0 and choice<=6:
                break
            else:
                print("Please choose a function from the menu.")
        except:
            print("Please enter a positive number")
    return choice

def inputnum():
    while True:
        try:
            n=int(input("Enter a number: "))
            return n
        except:
            print("Please enter a number.")

def getinputnum():
    while len(numberlist)<100:
        n=inputnum()
        if n==0:
            break
        else:
            numberlist.append(n)
    if len(numberlist)==100:
        print("List is full")
    return numberlist

def searchvalueinlist():
    n=inputnum()
    num=list()
    if n not in numberlist:
        print("The number you search is not in the list")
    else:
        for i in range (len(numberlist)):
            if n == numberlist[i]:
                num.append(i+1)
        print("The position in the list: ",num)

def highestnumber():
    max=numberlist[0]
    for i in range(len(numberlist)):
        if numberlist[i]>max:
            max=numberlist[i]
    return max

def removevalue():
    n=inputnum()
    if n not in numberlist:
        print("The number is not in the list")
    else:
        for i in range(len(numberlist)):
            if n in numberlist:
                numberlist.remove(n)
    print(n,"has been removed")
def sorting():
    numberlist.sort()
    return numberlist

def checklist():
    res=True
    if len(numberlist)<1:
        res=False
    return res

#main program:
while True:
    select=menu()
    if select==1:
        numberlist=getinputnum()
    if select==2:
        if checklist():
            searchvalueinlist()
        else:
            print("You need to input a list from function 1 in the menu")
    if select==3:
        if checklist():
            print("The highest valus in the list: ",highestnumber())
        else:
            print("You need to input a list from function 1 in the menu")
    if select==4:
        if checklist():
            removevalue()
        else:
            print("You need to input a list from function 1 in the menu")
    if select==5:
        if checklist():
            print(sorting())
        else:
            print("You need to input a list from function 1 in the menu")
    if select==6:
        exit()
