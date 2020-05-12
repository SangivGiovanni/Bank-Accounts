from Account import Account


class Current(Account):

    def __init__(self, acct_no, opening_deposit):
        super().__init__(acct_no, opening_deposit)

    def __str__(self):
        return f'Current Account #{self.acct_no} \nBalance: {Account.__str__(self)}'
