#!usr/bin/python3
class BankAccount:
    # Class variable
    bank_name = "Tech4Girls Bank"
    
    # Initializer method (__init__) to set up instance variables
    def __init__(self, account_holder):
        self.account_holder = account_holder
        self.balance = 0  # Initial balance set to 0

    # Instance method to deposit money
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount}. New balance: ${self.balance}")
        else:
            print("Deposit amount must be greater than zero.")

    # Instance method to withdraw money
    def withdraw(self, amount):
        if amount > 0 and self.balance >= amount:
            self.balance -= amount
            print(f"Withdrew ${amount}. New balance: ${self.balance}")
        else:
            print("Insufficient funds or invalid withdrawal amount.")

    # Static method to display bank policy
    @staticmethod
    def bank_policy():
        print("Welcome to Tech4Girls Bank. Our policy is to ensure customer satisfaction and security.")

    # Class method to get the bank name
    @classmethod
    def get_bank_name(cls):
        return cls.bank_name


# Demonstrating the usage of the class and its methods

# Creating an instance of BankAccount
account1 = BankAccount("Alice")

# Depositing money into account
account1.deposit(500)

# Withdrawing money from account
account1.withdraw(200)

# Calling the static method to print the bank policy
BankAccount.bank_policy()

# Calling the class method to get the bank name
print(f"Bank Name: {BankAccount.get_bank_name()}")

# Creating another account instance
account2 = BankAccount("Bob")

# Depositing money into account2
account2.deposit(1000)
account2.withdraw(150)