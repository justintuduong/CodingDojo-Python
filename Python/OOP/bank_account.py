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

justin = BankAccount(1/100, 1000)
jack = BankAccount(2/100, 500)

print(justin.deposit(50).deposit(60).deposit(70).withdraw(100).yield_interest().display_account_info())

print(jack.deposit(100).deposit(2000).deposit(3000).withdraw(200).withdraw(200).withdraw(200).withdraw(200).yield_interest().display_account_info())


