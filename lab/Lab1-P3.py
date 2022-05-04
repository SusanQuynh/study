#Yearly Personal Income Tax
#Personal pending amount(pa)
pa=9000000
#Alimony for each his/her dependent(pd)
pd=3600000

try: 
    income = int(input("Enter your year income: "))
    n=int(input("Enter dependent: "))
except:
    print("Must be a number")
    income = int(input("Enter your year income again: "))
    n=int(input("Enter dependent again: "))
incometax=0  
tf=12*(pa+n*pd)
print("Tax-free income: ",tf)
ti = income - tf
if ti<=0:
    ti=0
print ("Taxable income:",ti)
if ti<=0:
    incometax=0
else:
    if 0<ti<=5000000:
        incometax = ti*(5/100)
    elif ti<=10000000:
        incometax= 5000000*(5/100)+(ti-5000000)*(10/100)
    elif ti<=18000000:
        incometax = 5000000*(5/100)+(10000000-5000000)*(10/100) +(ti-1000000)*(15/100)
    else:
        incometax = 5000000*(5/100)+(10000000-5000000)*(10/100) + (18000000-10000000)*(15/100) + (ti-18000000)*(20/100)
print("Your yearly personal income tax is: ",incometax)
