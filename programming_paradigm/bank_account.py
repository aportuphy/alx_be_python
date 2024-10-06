# bank_account.py

class BankAccount:
    def __init__(self, initial_balance=0):
        """Initialize the account with an optional starting balance."""
        self.account_balance = initial_balance

    def deposit(self, amount):
        """Add money to the account balance."""
        self.account_balance += amount

    def withdraw(self, amount):
        """Withdraw money if the account has enough balance."""
        if amount > self.account_balance:
            return False
        self.account_balance -= amount
        return True

    def display_balance(self):
        """Print the current balance with two decimal places."""
        print(f"Current Balance: ${self.account_balance:.2f}")
