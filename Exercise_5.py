class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount:.2f}")
        else:
            print("Error: Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Error: Insufficient funds.")
        elif amount <= 0:
            print("Error: Withdrawal amount must be positive.")
        else:
            self.balance -= amount
            print(f"Withdrew ${amount:.2f}")

    def get_balance(self):
        return self.balance

class SavingAccount(BankAccount):
    def add_interest(self, rate):
        if rate > 0:
            interest = self.balance * (rate / 100)
            self.balance += interest
            print(f"Interest added: ${interest:.2f}")
        else:
            print("Error: Interest rate must be positive.")

# 🧑‍💻 Get user input
owner = input("Enter account owner's name: ")

try:
    initial_balance = float(input("Enter initial balance: "))
    account_type = input("Choose account type (bank or saving): ").strip().lower()

    if account_type == "saving":
        account = SavingAccount(owner, initial_balance)
    else:
        account = BankAccount(owner, initial_balance)

    while True:
        action = input("\nChoose action (deposit, withdraw, balance, interest, exit): ").strip().lower()

        if action == "deposit":
            amount = float(input("Enter deposit amount: "))
            account.deposit(amount)

        elif action == "withdraw":
            amount = float(input("Enter withdrawal amount: "))
            account.withdraw(amount)

        elif action == "balance":
            print(f"Current balance: ${account.get_balance():.2f}")

        elif action == "interest":
            if isinstance(account, SavingAccount):
                rate = float(input("Enter interest rate (%): "))
                account.add_interest(rate)
            else:
                print("Error: Interest can only be added to a saving account.")

        elif action == "exit":
            print("Thank you for using the bank system.")
            break

        else:
            print("Invalid action. Please try again.")

except ValueError:
    print("Error: Please enter valid numeric values.")