def getinput():
    while True:
        try:
            x= input("Enter the sentence: ")
        except:
            print("Invalid")
        break
    return x

def reorganisesentence(x):
    word= x.split(' ')
    n= len(word)
    n-=1
    while n>=0:
        print(word[n], end= ' ')
        n-=1

# chuong trinh chinh:
s = getinput()
reorganisesentence(s)

