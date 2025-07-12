class Atm:
  def __init__(self):
    self.pin =""
    self.balance = 0
    self.menu()

  def menu(self):
    user_input = input(""" 
    hello how can i help you?
    1.press 1 to create pin
    2.press 2 to change pin
    3.press 3 to check balance
    4.press 4 to withdraw
    5.press anything to exit
    """)
    if user_input == "1":
      # create pin 
      self.create_pin()
    elif user_input == "2":
       #change the pin
      self.change_pin()
    elif user_input == "3":
       #check balance
      self.check_balance()      
    elif user_input == "4":
      # withdraw 
      self.withdraw()
    else:
      exit()  

  def create_pin(self):
    user_pin = input("enter your pin") 
    self.pin = user_pin

    user_balance = int(input("enter balance"))
    self.balance = user_balance

    print("pin created successfully")
    self.menu()

  def change_pin(self):
    old_pin = input("enter old pin")
    if old_pin == self.pin:
      # let him chnange the pin
      new_pin = input("enter new pin")
      self.pin = new_pin
      print("pin change successfully")
    else:
      print("nai karne de sakta re baba")
      self.menu()

  def check_balance(self):
    user_pin = input("enter your pin")  
    if user_pin == self.pin:
      print("your balance is" , self.balance)
    else:
      print("chal nikal yahan se")  
      self.menu()

  def withdraw(self): 
    user_input = input("enter the pin") 
    if user_input == self.pin:
      #allow to withdraw
      amount = int(input("enter the amount"))
      if amount <= self.balance:
        self.balance = self.balance - amount
        print("withdraw successfully is " , self.balance)
      else:
        print ("abe garib")  
    else:
        print("sale chor")  
        self.menu()
obj = Atm()






     