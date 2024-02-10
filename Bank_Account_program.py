class Bank_Account:
    def __init__(self, name, balance=0):
        self.name = name
        self.balance = balance
    def  deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount}. New balance {self.balance}")
    def withdraw (self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print(f"Withdrew {amount}. New balance {self.balance}")
        else:
            print(f"Insufficient funds. {self.balance}")
            
# Existing accounts
account1 = Bank_Account("Lorine Abdul", 120000)
account2 = Bank_Account("Doreen Arielle", 10000)
account3 = Bank_Account("David Ouma", 100000000)

# Activities
account1.withdraw(8560)
account2.deposit(30555)
account3.withdraw(200000000)

        