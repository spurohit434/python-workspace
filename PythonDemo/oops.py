class BankAccount:
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder  # Public attribute
        self.__balance = balance  # Private attribute

    # Public method to deposit money
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited ${amount}. New balance: ${self.__balance}")
        else:
            print("Invalid deposit amount.")

    # Public method to withdraw money
    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrew ${amount}. New balance: ${self.__balance}")
        else:
            print("Invalid withdrawal amount or insufficient funds.")

    # Public method to get the balance (abstracted access to private attribute)
    def get_balance(self):
        return self.__balance

# Creating an object of the BankAccount class
account = BankAccount("John Doe", 1000)

# Accessing public methods
account.deposit(500)  # Deposited $500. New balance: $1500
account.withdraw(200)  # Withdrew $200. New balance: $1300

# Accessing public attribute
print(f"Account holder: {account.account_holder}")  # Account holder: John Doe

# Accessing private attribute directly (not recommended and will cause an error)
print(account._BankAccount__balance)  # AttributeError: 'BankAccount' object has no attribute '__balance'

# Accessing private attribute through a public method
print(f"Current balance: ${account.get_balance()}")  # Current balance: $1300