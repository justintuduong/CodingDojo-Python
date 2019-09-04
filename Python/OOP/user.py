class User:
    
    def __init__(self, full_name, balance):
        self.name = full_name
        self.balance = 0

    def make_deposit(self, amount):
        self.balance += amount
        print(f"{self.name}, your balance is: ${self.balance}")
        return self
    
    def make_withdrawal(self, amount):
        self.balance -= amount
        print(f"{self.name}, your balance is: ${self.balance}")
        return self
    
    def display_user_balance(self):
        self.balance
        print(f"{self.name}, your balance is: ${self.balance}")
        return self
    
    def transfer_money(self, recipient, amount):
        self.balance -= amount
        recipient.balance += amount
        print(f"{self.name}, you have transfer over {amount}. Your current balance is: ${self.balance}")
        return self


justin = User("Justin Duong", 0)
cameron = User("Cameron Lee", 0)
kaysee = User("Kayee", 0)

print(justin.make_deposit(100).make_deposit(200).make_deposit(300).make_withdrawal(100).display_user_balance())
print(kaysee.make_deposit(300).make_withdrawal(20).make_withdrawal(20).make_withdrawal(20).display_user_balance())
print(justin.transfer_money(kaysee,200))
      
      
      
      
#print(justin.make_deposit(500))
#print(justin.make_deposit(500))
#print(justin.make_withdrawal(200))
#print(justin.display_user_balance())
#print(kaysee.make_deposit(300))
#print(kaysee.make_withdrawal(20))
#print(kaysee.make_withdrawal(20))
#print(kaysee.make_withdrawal(20))
#print(kaysee.display_user_balance())
#print(justin.transfer_money(kaysee,200))
#print(kaysee.display_user_balance())

