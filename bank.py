import re


class Account:
    country = "Kenya",
    
    def __init__(self,name,number):
        
        self.name = name
        self.balance= 0
        self.number = number
        self.deposit=[]
        self.withdraw=[]
        self.transaction=100
      
    
    def depositing(self,amount):
        if amount<=0:
            return f"deposit amount is greater than zero"
        else:
            self.deposit.append(amount)

            self.balance+=amount
            return f"Dear {self.name} you've deposited {amount} and your balance is {self.balance} {self.deposit}"
    
    
    def withdrawals(self,amount):
        transaction_fee = 100
        if amount > self.balance:
            return f"insufficient funds"
        elif amount<=0:
            return f"amount must be greater than 0"
        else:
            self.balance-=amount
            self.balance-=transaction_fee
            self.withdraw.append(amount)
            return f"hello {self.name} you have withdrawn {amount} your new balance is {self.balance}"
            
    def deposit_statement(self):
        for amount in self.deposit:
            print (f"Here is your ministatement: {amount}")
            
    def withdraw_statement(self):
        for amount in self.withdraw:
            print (f"here is your ministatement: {amount}")
    
    def current_balance(self):
        return f"your current balance is : {self.balance}"
        