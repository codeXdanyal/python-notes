class Account:
    def __init__(self, bal, acc_no):
        self.bal = bal
        self.acc = acc_no
        self.transaction = []

    def debit(self, balance):
        if balance > self.bal:
            print("Insufficient Fund")
        else:
            self.bal -= balance
            self.transaction.append(f"Debited Rs: {balance}")
            print(f"Rs {balance} was debited")
            print(f"total balance = {self.bal}")

    def credit(self, balance):
        self.bal += balance
        print(f"Rs {balance} was credited")
        print(f"total balance = {self.bal}")

    def check_balance(self):
        print(f"Your total balance is: {self.bal}")

    def transaction_history(self):
        for val in self.transaction:
            print(val)


acc1 = Account(100000, 61682)
acc1.debit(40000)
acc1.debit(30000)
acc1.debit(40000)
acc1.credit(9000)
acc1.transaction_history()
acc1.check_balance()
