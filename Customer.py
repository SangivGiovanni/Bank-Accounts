from Current import Current
from Savings import Savings
from Business import Business


class Customer:
    def __init__(self, name, pin):
        self.name = name
        self.pin = pin

        self.accts = {'C': [], 'S': [], 'B': []}

    def __str__(self):
        return self.name

    def open_current(self, acct_no, opening_deposit):
        self.accts['C'].append(Current(acct_no, opening_deposit))

    def open_savings(self, acct_no, opening_deposit):
        self.accts['S'].append(Savings(acct_no, opening_deposit))

    def open_business(self, acct_no, opening_deposit):
        self.accts['B'].append(Business(acct_no, opening_deposit))

    def get_total_deposits(self):
        total = 0
        for acct in self.accts['C']:
            print(acct)
            total += acct.balance
        for acct in self.accts['S']:
            print(acct)
            total += acct.balance
        for acct in self.accts['B']:
            print(acct)
            total += acct.balance
        print(f'Total Deposits: £{total:.2f}')


def make_dep(cust, acct_type, acct_no, dep_amt):

    for acct in cust.accts[acct_type]:
        if acct.acct_no == acct_no:
            acct.deposit(dep_amt)


def make_wd(cust, acct_type, acct_no, wd_amt):

    for acct in cust.accts[acct_type]:
        if acct.acct_no == acct_no:
            acct.withdraw(wd_amt)

