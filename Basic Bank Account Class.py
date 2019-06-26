class Account:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, dep_amt):
        self.balance = self.balance + dep_amt
        print(f"Added {dep_amt} to the balance")

    def withdrawal(self, wd_amt):
        if self.balance >= wd_amt:
            self.balance = self.balance - wd_amt
            print("Withdrawal succesfull")
        else:
            print("Not enough funds")

    def __str__(self):
        return f'Owner is: {self.owner}\nCurrent balance is: {self.balance}'


acct1 = Account('Jose', 100)

print(acct1)

acct1.deposit(500)

print(acct1)
print(acct1.owner)
print(acct1.balance)

acct1.withdrawal(500)
acct1.withdrawal(500)
