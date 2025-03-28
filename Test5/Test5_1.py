class Account:
    def __init__(self, account_number, account_type, interest_rate=0):
        self.balance = 0
        self.account_number = account_number
        self.account_type = account_type
        self.interest_rate = interest_rate

    def deposit(self, amount):
        # Complete the code to handle a deposit by adding to the balance.
        self.balance += amount
        pass

    def withdraw(self, amount):
        # Complete the code to handle a withdrawal by subtracting from the balance.
        if amount > self.balance:
            print("Insufficient funds. Withdrawal canceled.")
        else:
            self.balance -= amount
        pass

    def getBalance(self):
        return self.balance

    def getAccountType(self):
        return self.account_type

    def getAccountNumber(self):
        return self.account_number

    def applyInterest(self):
        interest_applied = self.balance * self.interest_rate
        self.balance += interest_applied
        return interest_applied

class CheckingAccount(Account):
    def __init__(self, account_number):
        Account.__init__(self, account_number, "Checking")

class SavingsAccount(Account):
    def __init__(self, account_number, interest_rate=0.05):
        Account.__init__(self, account_number, "Savings", interest_rate)

accounts = {
    "C": CheckingAccount(1000),
    "S": SavingsAccount(1001)
}

done = False
while not done:
    account_choice = input("Enter (C)hecking or (S)avings account, or (Q) to quit: ").upper()
    if account_choice == "Q":
        break
    account = accounts.get(account_choice, None)
    if account_choice is None:
        print(f"Invalid account choice {account_choice}.")
        continue
    transaction = input("Enter (D)eposit, (W)ithdraw, or (A)pply Interest: ").upper()
    if transaction == "A":
        amount = account.applyInterest()
        print(f"Applied interest of {amount:.2f} to balance")
    else:
        amount = float(input("Enter amount of transaction: "))
        if transaction == "D":
            account.deposit(amount)
        elif transaction == "W":
            account.withdraw(amount)
        else:
            print(f"Invalid transaction choice {transaction}")
            continue
    print(f"Account number {account.getAccountNumber()} type {account.getAccountType()} Balance {account.getBalance():.2f}")