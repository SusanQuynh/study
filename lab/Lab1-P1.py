# input month to find out the season of the year
try:
    month = int(input("Enter month: "))
    if month<=0 or month >12:
        print("There is no season in a year")
    if 1<=month and month<=3:
        print("Spring")
    if 3<month<=6:
        print("Summer")
    if 6<month<=9:
        print("Fall")
    if 9<month<=12:
        print("Winter")
except:
    print("Month must be a positive number")
    
