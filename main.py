class BankAccount:
    def __init__(self, account_number, account_holder_name, initial_balance=0):
        self._account_number = account_number
        self._account_holder_name = account_holder_name
        self._account_balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self._account_balance += amount
            return f"Deposited ${amount}. New balance: ${self._account_balance}"
        else:
            return "Invalid deposit amount. Please enter a positive number."

    def withdraw(self, amount):
        if amount > 0 and amount <= self._account_balance:
            self._account_balance -= amount
            return f"Withdrew ${amount}. New balance: ${self._account_balance}"
        elif amount <= 0:
            return "Invalid withdrawal amount. Please enter a positive number."
        else:
            return "Insufficient funds for withdrawal."

    def display_balance(self):
        return f"Account Balance for {self._account_holder_name}: ${self._account_balance}"

my_account = BankAccount("12345", "John Doe", 1000)
print(my_account.display_balance()) 
print(my_account.deposit(500))      
print(my_account.withdraw(200))     
print(my_account.display_balance())  