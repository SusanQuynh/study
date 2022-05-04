def getinput():
    while True:
        try:
            word=input("Enter string: ")
        except:
            print("Invalid")
        break
    return word

def counting():
    x = getinput()
    char=0
    digit=0
    specialchar=0
    for letter in x:
        if letter.islower() or letter.isupper():
            char+=1
        elif letter.isdigit():
            digit+=1
        else:
            specialchar+=1
    print("Character: ",char)
    print("Digit: ",digit)
    print("Special character: ",specialchar)

#chuong trinh chinh:
counting()
