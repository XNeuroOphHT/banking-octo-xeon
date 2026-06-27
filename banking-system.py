class Account:
    def __init__(self, username, password, account_id, full_name, balance=0.0):
        self.username = username
        self.password = password
        self.account_id = account_id
        self.full_name = full_name
        self.balance = balance

    def authenticate(self, username, password):
        return self.username == username and self.password == password

    def display_info(self):
        print("\nAccount Details")
        print(f"Name: {self.full_name}")
        print(f"Username: {self.username}")
        print(f"Account ID: {self.account_id}")
        print(f"Balance: ${self.balance:.2f}")

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited: ${amount:.2f}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew: ${amount:.2f}")
        else:
            print("Insufficient funds or invalid withdrawal amount.")


class BankingSystem:
    def __init__(self):
        self.accounts = {}

    def create_account(self, username, password, account_id, full_name, balance=0.0):
        if username in self.accounts:
            print("Username already exists.")
            return None

        account = Account(username, password, account_id, full_name, balance)
        self.accounts[username] = account
        print("Account created successfully.")
        return account

    def login(self, username, password):
        account = self.accounts.get(username)
        if account and account.authenticate(username, password):
            print("Login successful.")
            return account
        print("Invalid username or password.")
        return None


if __name__ == "__main__":
    bank = BankingSystem()

    # Placeholder account example
    bank.create_account(
        username="Huzaifa Faisal",
        password="HuZ@1F$",
        account_id="ACC-1001",
        full_name="Huzaifa Faisal",
        balance=1000.0,
    )

    account = bank.login("Huzaifa Faisal", "HuZ@1F$")
    if account:
        account.display_info()

        try:
            deposit_amount = float(input("Enter deposit amount: "))
            account.deposit(deposit_amount)
        except ValueError:
            print("Invalid deposit amount.")

        try:
            withdraw_amount = float(input("Enter withdrawal amount: "))
            account.withdraw(withdraw_amount)
        except ValueError:
            print("Invalid withdrawal amount.")

        account.display_info()
    else:
        print("Login failed. Please try again.")