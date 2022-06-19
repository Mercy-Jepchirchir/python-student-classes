from datetime import datetime

date = datetime.now()



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
            my_details= {"date":date.strftime("%d,%m,%H"),"amount":amount,"narration":"thankyou for depositing"}
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
            details= {"date":date.strftime("%d,%m,%H"),"amount":amount,"narration":"thank you,for withdrawing "}
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
            
        
            
        
       
            
    
        
        

        
    
        