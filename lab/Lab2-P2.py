#greatest common diviser:
def gcd(a, b):
    if (b == 0):
        return a;
    return gcd(b,a % b)
def commonprimediviser(a,b):
    i=1
    j=1
    print("Common divisier",end=': ')
    while i<=a/2 or j<=b/2:
        if a%i==0 and b%j == 0:
            print(i, end=',')
            i+=1
            j+=1
        else:
            i+=1
            j+=1
            continue
#least common multiple:
def lcm(a,b):
    lcm=a*b/gcd(a,b)
    return lcm
try:
    m=int(input("Enter m: "))
    n= int(input("Enter n: "))
    print(commonprimediviser(m,n))
    print("GCD: ",gcd(m,n))
    print("LCM: ",lcm(m,n))
except:
    print("Invalid")

