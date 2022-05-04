def multiplication():
    a=n
    for i in range(1,11):
        result=i*a
        print(i," x ",a," = ",result)
try:
    n=int(input("Enter n: "))
    while True:
        if n>1 and n<=9:
            print(multiplication())
            break
        else:
            n=int(input("Re-enter n: "))
except:
    print("Invalid")




