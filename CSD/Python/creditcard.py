# A customer's credit card.
class CreditCard():
    #Create new customer's credit card
    def __init__(self,name=None,bank=None,account=None,limit=None):
        self._name=name
        self._account=account
        self._bank=bank
        self._limit=limit
        self._balance=0
    def desposit(self,amount):
        if self.balance + amount > self.limit:
            print("Out of limit.")
        else:
            self.balance += amount
    def withdraw(self,mount):
        if self.balance < mount:
            print("You don't have enough money. Poor man!")
        else:
            self.balance-=mount
    def display(self):
        print(self.name, " - ", self.account, " - ",self.bank, " - ", self.limit, " - ",self.balance)
bk=CreditCard("dfsd","fsdf","454sdfd",45646)
bk.display()
    
    
