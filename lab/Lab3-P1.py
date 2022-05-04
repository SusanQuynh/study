import random
def Totalsought():
    x= random.randint(2,12)
    return x

def dice():
    x= random.randint(1,6)
    return x

def sum2dice():
    x=Totalsought()
    print("Total sought: ", x)
    count=1
    res=True
    while res:
        a = dice()
        b = dice()
        if (a+b) != x:
            print("Result of ", count, " throw: ", a, " + ", b)
            count += 1
            res=True
        else:
            print("Result of ", count, " throw: ", a, " + ", b)
            print("You got your total sought in ", count, " throws!")
            res = False

#Chuong trinh chinh:
print("Dice Thrower")
print("=========================")
sum2dice()

