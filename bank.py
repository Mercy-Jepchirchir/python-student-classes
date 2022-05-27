class Account:
    country = "Kenya",
    
    def __init__(self,branch_name,accountnumber,balance,idnumber):
        
        self.branch_name=branch_name
        self.balance= balance
        self.accountnumber=accountnumber
        self.idnumber=idnumber
    
    def deposit(self):
        deposit_amount = int(input("enter amount to deposit:"))
        deposit_amount+=self.balance
        return f"your balance is {deposit_amount}"
    
    def withdraw(self):
        withdraw_amount = int(input("enter amount to withdraw:"))
        self.balance-=withdraw_amount
        return f"your balance is {self.balance}"