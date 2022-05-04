# Arrage 3 real number in asceding order.
max = 0
min = 0
center = 0
try:
    a=int(input("Enter a: "))
    b=int(input("Enter b: "))
    c=int(input("Enter c: "))
    if a>b and a>c:
        max = a
        if b>c:
            min =c
            center =b
        else:
            min = b
            center = c
    if a<b and b>c:
        max = b
        if a>c:
            min =c
            center =a
        else:
            min = a
            center =c
    if c>b and a<c:
        max = c
        if b>a:
            min =a
            center =b
        else:
            min = b
            center = a
    if a==b and a>c:
        max=center=a
        min=c
    if a==c and a>b:
        max =center=a
        min =b
    if b==c and b>a:
        max= center=b
        min = a
    if a==b==c:
        max=center=min=a
except:
    print("Need a number")

finally:
    print(min," ; ",center," ; ", max)
