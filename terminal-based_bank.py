#terminal bank account
#application of class, init methods, instance methods, objects etc
class BankAccount:
  def __init__(self, first_name, last_name, account_id, account_type, pin, balance):
    self.first_name = first_name
    self.lastname = last_name
    self.account_id = account_id
    self.account_type = account_type
    self.pin = pin
    self.balance = balance
  
  def login(self):
    self.first_name = input("First name: ")
    self.last_name = input("Last name: ")
    self.pin = int(input("Enter PIN: "))
    return self

  def deposit(self, amount):
    amount = 0
    temp_pin = int(input("Enter your PIN: "))
    if temp_pin == self.pin:
      amount = int(input("Enter amount to deposit: "))
      self.balance += amount
      return self
    else:
      print("Invalid Pin")
        
  def withdraw(self, amount):
    amount = 0
    temp_pin = int(input("Enter your PIN: "))
    if temp_pin == self.pin:
      amount = int(input("Enter amount to withdraw: "))
      self.balance -= amount
      return self
  
  def display_balance(self):
    print(f"Hello, {self.first_name} {self.last_name}! Your current balance is {self.balance}")
      
user1 = BankAccount('', '', 0, '', 0, 0)

print("Welcome to your bank account!")
user1.login()
while True:
  decision = int(input("(1) Deposit, (2) Withdraw, (3) Display Balance or (4) Quit: "))
  if decision == 1:
    user1.deposit(0)
  elif decision == 2:
    user1.withdraw(0)
  elif decision == 3:
    user1.display_balance()
  elif decision == 4:
    print(f"Goodbye")
  else:
    print("invalid choice")

    