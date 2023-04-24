# class OOP
class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("Not enough funds")

# membuat objek
my_account = BankAccount("John Doe", 1000)

# memanggil method objek
my_account.deposit(500)
print(my_account.balance) # output: 1500
my_account.withdraw(2000) # output: Not enough funds
