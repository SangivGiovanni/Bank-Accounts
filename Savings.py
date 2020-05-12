from Account import Account


class Savings(Account):

    def __init__(self, acct_no, opening_deposit):
        super().__init__(acct_no, opening_deposit)

    def __str__(self):
        return f'Savings Account #{self.acct_no}\n Balance: {Account.__str__(self)}'
