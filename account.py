class BankAcount:
  
  def __init__(self, first_name, last_name,bank):
    self.first_name=first_name
    self.last_name=last_name
    self.bank=bank
    self.balance=0
    self.phone_number=0
    self.deposits=[]
    self.withdrawals=[]
    self.loans=0
    
  def account_name(self):
    name="{} account for {} {}".format(self.bank, self.first_name, self.last_name )
    return name
    
  def deposit (self, amount):
      if amount <=0:
          print("Sorry that amount is less")
      else:
        self.balance += amount
        print("You have deposited {} to your {}".format(amount,self.account_name())) 
    
     
  def get_balance(self, amount):
      return "Balance for {} is {}".format(self.account_name(),self.balance)
      
    
  def withdraw(self, amount):
    if amount <= 0:
        print("You can not withdraw that amount")

    elif amount > self.balance:
        print ("Your balance is low.:", amount)
      
    else:
        self.balance -= amount
        print ("You have withdrawn amount from {}".format(self.account_name()))
        return
      
  def withdraw_stementst(self):
      withdraw=withdraw.append(withdraw())
      return withdraw
  
  def loans(self,amount):
      self.loans= self.loans
      print("A loan of {} has been deposited to {}:".format(amount,self.account_name()))
      
      
  def loan_repayment(self,amount):
      if amount >=1:
          self.repay=self.loans-amount
          print("This amount{}has been used to repay your loan".format(amount))
          print("The loan balance is {}".format(self.repay))
          