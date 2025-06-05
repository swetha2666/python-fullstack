from abc import ABC,abstractmethod
class Account():
    @abstractmethod
    def get_account():
        pass

    @abstractmethod
    def deposit():
        pass

    @abstractmethod
    def withdraw():
        pass

class Saving_account(Account):
    __balance=0
    owner=0

    def get_balance(self):
        return self.__balance
    
    
    def deposit(self,amount):
        self.__balance += amount
        print("deposit amount:",amount)

    def withdraw(self,amount):
        self.__balance -= amount
        print("withdraw amount:", amount)
        
class Current_account(Account):
    __balance=0
    owner=0
    withdraw_limit=0
     
    def __init__(self,limit):
        self.withdraw_limit=limit


    def get_balance(self):
        return self.__balance
    
    
    def deposit(self,amount):
        self.__balance += amount
        print("deposit amount:",amount)

    def withdraw(self,amount):
        if amount> self.__balance:
            print("no balance")
        if amount<self.__balance: 
            self.__balance -= amount
            print("withdraw amount:", amount)
class Bank:
    owner="lucky" 
    account_number=0
    def __init__(self,name,number,account_type="saving"):
        self.owner=name
        self.account_number=number
        if account_type == "saving":
            self.account=Saving_account()
        if account_type == "current":
            self.account = Current_account(500)
class Manager:
    def get_customer_info(self,bankAccount=Bank):
        print(f"customer name:{bankAccount.owner}")
        print(f"account_number:{bankAccount.account_number}")
        print(f"account_type: ",end=" ")
        if (type(bankAccount.account)==Saving_account):
            print("saving account")
        else:
            print("current account")
        print(f"bank balance: {bankAccount.account.get_balance()}")
    def __str__(self):
        return "bye"
nam=Bank('swetha',6126,"saving")
nam.account.deposit(200)

sam=Bank("nikky",8822,"current")
sam.account.withdraw(100)
print(nam)
        

s=Manager()

print("====swetha account====")
s.get_customer_info(nam)
 
print("====nikky account====")
s.get_customer_info(sam)


    
    
