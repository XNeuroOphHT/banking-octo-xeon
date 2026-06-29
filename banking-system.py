class BankAccount:
    def __init__(self, account_number, owner, balance=0):
        self.account_number = account_number
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"{self.owner} deposited {amount}. New balance: {self.balance}")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"{self.owner} withdrew {amount}. New balance: {self.balance}")
        else:
            print("Insufficient funds!")

    def check_balance(self):
        print(f"Account {self.account_number} ({self.owner}) balance: {self.balance}")


class Bank:
    def __init__(self):
        self.accounts = {}
        self.users = {}  # store login info

    def create_account(self, account_number, owner, username, password, code, balance=0):
        if account_number in self.accounts:
            print("Account number already exists!")
        else:
            self.accounts[account_number] = BankAccount(account_number, owner, balance)
            self.users[username] = {"password": password, "code": code, "account": account_number}
            print(f"Account created for {owner} with number {account_number}")

    def login(self, username, password, code):
        user = self.users.get(username)
        if user and user["password"] == password and user["code"] == code:
            print("Login successful!")
            return self.accounts[user["account"]]
        else:
            print("Login failed!")
            return None


# --- Program Flow ---
bank = Bank()
bank.create_account(101, "Huzaifa", "huzaifa", "1234", "9999", 1000)
bank.create_account(102, "Ali", "ali", "abcd", "8888", 500)

# Login
username = input("Enter username: ")
password = input("Enter password: ")
code = input("Enter security code: ")

account = bank.login(username, password, code)

if account:
    while True:
        print("\n--- Banking Menu ---")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Check Balance")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            amt = int(input("Enter amount to deposit: "))
            account.deposit(amt)
        elif choice == "2":
            amt = int(input("Enter amount to withdraw: "))
            account.withdraw(amt)
        elif choice == "3":
            account.check_balance()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice!")