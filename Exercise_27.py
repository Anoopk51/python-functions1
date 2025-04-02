'''<-----------My Attempt-------------->'''
# class Bank_Account:
#     def __init__(self,name,balance):
#         self.name=name
#         self.balance=balance
#     def Deposit(self,deposit):
#         self.balance=self.balance+deposit
#         print(f'Your total bank balance is {self.balance}rs.')
        
#     def Withdraw(self,withdraw):
#         if self.balance>withdraw:
#             self.balance=self.balance-withdraw
#             print(f'After withdraw {withdraw}rs , Now total save balance is {self.balance}rs. ')
#         else:
#             print(f'Sorry! In your account no have {withdraw}rs.')
# account=Bank_Account('Anoop Kushwaha',10000)
# account.Deposit(5000)
# account.Withdraw(16000)


'''<-------------Ma'an Aproch or solution---------->'''
class BankAccount:
    def __init__(self,name,balance=0):
        self.account_holder=name
        self.balance=balance
    def deposit(self,amount):
        self.balance=self.balance+amount
        print(f"Deposited {amount} to your account")
    def withdraw(self,amount):
        if amount>self.balance:
            print("Not enough balance!!")
        else:
            self.balance=self.balance - amount
    def __str__(self):
        return f'Account Holder Name: {self.account_holder} \nBalance: {self.balance}'
obj=BankAccount("Ramesh",1000)
print(obj)
obj.deposit(200)
obj.withdraw(500)
print(obj)
obj.withdraw(100)
print(obj)