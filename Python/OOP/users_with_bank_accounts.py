class User:
    
    def __init__(self, full_name, account):
        self.name = full_name
        self.balance = 0
        self.account = BankAccount(int_rate=0.02, balance=0)

    def make_deposit(self, amount):
        self.account.balance += amount
        print(f"{self.name}, your balance is: ${self.account.balance}")
        return self
    
    def make_withdrawal(self, amount):
        self.account.balance -= amount
        print(f"{self.name}, your balance is: ${self.account.balance}")
        return self
    
    def display_user_balance(self):
        self.account.balance
        print(f"{self.name}, your balance is: ${self.account.balance}")
        return self
    
    def transfer_money(self, recipient, amount):
        self.account.balance -= amount
        recipient.account.balance += amount
        print(f"{self.name}, you have transfered over {amount} to your recipient. Your current balance is: ${self.account.balance}")
        return self

class BankAccount:
    def __init__(self, int_rate, balance):
        self.int_rate = int_rate
        self.balance = balance
    
    def deposit(self, amount):
        self.balance += amount
        print(f'Your current balance is: $ {self.balance}')
        return self
    
    def withdraw(self, amount):
        if self.balance - amount < 0:
            print("Insufficient funds: Charging a $5 fee")
            self.balance - 5
        self.balance -= amount
        print(f'Your current balance is: $ {self.balance}')
        return self

    def display_account_info(self):
        print(f'Your current balance is: $ {self.balance}')
        return self
    
    def yield_interest(self):
        int = 0
        if self.balance > 0:
            int = self.balance * self.int_rate
        print(f'Interest accrued will be of $ {int}')
        return self

# justin = BankAccount(1/100, 1000)
# jack = BankAccount(2/100, 500)

justin = User("Justin Duong", 0)
cameron = User("Cameron Lee", 0)
kaysee = User("Kayee", 0)


print(justin.make_deposit(100).make_deposit(200).make_deposit(300).make_withdrawal(100).display_user_balance())
print(kaysee.make_deposit(300).make_withdrawal(20).make_withdrawal(20).make_withdrawal(20).display_user_balance())
print(justin.transfer_money(kaysee,200))