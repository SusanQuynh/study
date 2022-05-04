def sum(n):
    i=1
    sum=0
    x=n
    while i<=x:
        sum+=i
        i+=1
    return sum
def factorial(n):
    i = 1
    factorial=1
    x=n
    while i<=x:
        factorial*=i
        i+=1
    return factorial
def fraction(n):
    i = 1
    fraction=0
    x=n
    while i<=x:
        fraction+=1/i
        i+=1
    return fraction
def checkprime(n):
    res=1
    i=2
    x=n
    while i<=x//2:
        if x%i==0:
            res=0
            break
        else:
            i+=1
            continue
    if res==0:
        print("n is not a prime number")
    else:
        print("n is a prime number")
try:
    n=int(input("Enter n: "))
    while True:
        if n<=5:
            n=int(input("Re-enter n: "))
        else:
            print("Sum: ",sum(n))
            print("Factorial: ",factorial(n))
            print("Fraction sum: ",fraction(n))
            n=int(input("Reinput n: "))
            print(checkprime(n))
            break
except:
    print("Invalid")


