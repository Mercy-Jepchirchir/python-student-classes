from datetime import datetime
import re





class Account:
    country = "Kenya",
    
    def __init__(self,name,number):
        #Add a new attribute loan_balance which is zero by default.
        self.name = name
        self.balance= 0
        self.number = number
        self.deposit=[]
        self.withdraw=[]
        self.transaction=100
        self.loan_balance = 0
      
    
    def depositing(self,amount):
        if amount<=0:
            return f"deposit amount is greater than zero"
        else:
            my_details= {"date":datetime.now().strftime("%d,%m,%H"),"amount":amount,"narration":f"thankyou for depositing {amount} on {datetime.now()}"}
            self.deposit.append(my_details)
            
            self.balance+=amount
            return f"Dear {self.name} you've deposited {amount} and your balance is {self.balance} "
    
    
    def withdrawals(self,amount):
      
        transaction_fee = 100
        if amount+self.transaction > self.balance:
            return f"insufficient funds"
        elif amount<=0:
            return f"amount must be greater than 0"
        else:
            details= {"date":datetime.now().strftime("%d,%m,%H"),"amount":amount,"narration":f"thank you,for withdrawing {amount} at {datetime.now()}"}
            self.withdraw.append(details) 
            
            self.balance-=amount
            self.balance-=transaction_fee
            return f"hello {self.name} you have withdrawn {amount} your new balance is {self.balance}"
            
    def deposit_statement(self):
        for amount in self.deposit:
            print (f"Here is your ministatement: {amount}")
            
    def withdraw_statement(self):
        for amount in self.withdraw:
            print (f"here is your ministatement: {amount}")
    
    def current_balance(self):
        return f"your current balance is : {self.balance}"
    #Add a new method  full_statement which combines both deposits and withdrawals into one list ordered by date
    # and using a for loop prints each transaction in a new line like this
    #16/06/22 —----- Deposit —---- 1000
    def full_statement(self):
        dep_withdraw= self.deposit + self.withdraw
        for n in dep_withdraw:
            print (n)
    
#Add a borrow method which allows a customer to borrow if they meet these conditions:
#Customer has made at least 10 deposits.
#Loan amount requested must be more than 100
   #A customer qualifies for a loan amount that is less than  or equal to 1/3 of their total sum of deposit history
   #Customer account has no has no balance
   #Customer has no outstanding loan
    #The loan attracts  an interest of 3%.
    def borrow (self,amount):
        sum = 0
        for n in self.deposit:
            sum+=n["amount"]
        if len(self.deposit)<10:
            return f"Add more deposits"
        if amount <100:
            return f"inqure for more than 100 loan"
        if amount>sum/3:
            return f"Dear {self.name} you can borrow loan upto {sum/3} "
        if self.balance!=0:
            return f"Dear {self.name} you still have a balance of {self.balance}"
        if self.loan_balance!=0:
            return f"Dear {self.name} you still have a balance of {self.loan_balance}, hence repay to borrow"
        else:
            interest = amount*0.03
            self.loan_balance+=amount+interest
            return f"Dear {self.name} you have borrowed {self.loan_balance} and your balance is {self.balance}"
#Add a loan repayment method with these conditions
#A customer can repay a loan to reduce the current loan balance
#Overpayment of a loan increases a customers current deposit
    def loan_repayment(self,amount):
        if amount<0:
            return "amount is invalid " 
        if amount > self.loan_balance:
            self.balance+=amount-self.loan_balance
            return f"Dear {self.name}thank you for repaying your loan of {amount-self.loan_balance} and your account balance is {self.balance}"
        
        else:
            self.loan_balance-=amount
            return f"Dear {self.balance} thank you, you've loan of {amount} and your current loan balance is {self.loan_balance}"
            
            
   
#Add a new method transfer which accepts two attributes (amount and instance of another account). 
# If the amount is less than the current instances balance, the method transfers the requested
# amount from the current account to the passed account. The transfer is accomplished by reducing 
# the current account balance and depositing the requested amount to the passed account.
    def transfer(self,amount,instance_account):
        if amount<=0:
            return f"invalid"
        if amount>= self.balance:
            return f"insufficient amount in your account"
        if isinstance(instance_account,Account):
            self.balance-=amount
            instance_account.balance += amount
            return f"you have transfered {amount} to {instance_account} account with the name {instance_account.name} and your new balance is {self.balance}"
            
   

        
            
         
       
            
    
        
        

        
    
        