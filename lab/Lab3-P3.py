def menu():
    print("1.Removal all charaters from the string.")
    print("2.Removal special symbols/punctuation from thr string.")
    print("3.Quit")

    while True:
        try:
            choice=int(input("Choose a function from the menu: "))
            if choice >0 and choice <4:
                break
            else:
                print("Choose again.")
        except:
            print("Must enter an positive number.")
    return choice

def getinput():
    while True:
        try:
            word=input("Enter string: ")
        except:
            print=("Invalid")
        break
    return word

def removecharacter():
    chuoi = getinput()
    final= ''.join([i for i in chuoi if i.isdigit()])
    return final

def removepunctuation():
    chuoi = getinput()
    punctuation= '''~`!@#$%^&*()_+-=[]{}\|;':",./<>?'''
    final=""
    for char in chuoi:
        if char not in punctuation:
            final = final + char
    return final


#chuong trinh chinh:
while True:
    select = menu()
    if select == 1:
        print(removecharacter())
    if select == 2:
        print(removepunctuation())
    if select == 3:
        exit()




