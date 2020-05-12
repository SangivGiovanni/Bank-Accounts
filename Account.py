class Account:

    def __init__(self, acct_no, opening_deposit):
        self.acct_no = acct_no
        self.balance = opening_deposit

    def __str__(self):
        return f'£{self.balance:.2f}'

    def deposit(self, dep_amt):
        self.balance += dep_amt

    def withdraw(self, wd_amt):
        if self.balance >= wd_amt:
            self.balance -= wd_amt
            print(f'-£{wd_amt}')
            print(f'New Balance: £{self.balance:.2f}')
        else:
            print('Funds Unavailable')
