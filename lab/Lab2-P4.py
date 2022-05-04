try:
    ida = int(input("Enter the initial deposit amount: "))
    import random
    interest = random.uniform(0,1)
    while True:
        if ida >= 1000000:
                    n = int(input("Enter year want to deposit: "))
                    while True:
                        if n <= 0:
                            n = int(input("Re-enter year want to deposit: "))
                        else:
                            amount = ida * (1 + interest) ** n
                            print("Amount: ", amount)
                            break
                    break
        else:
            ida = int(input("Re-enter the initial deposit amount: "))
except:
    print("Invalid")


