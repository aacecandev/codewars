class User(object):
    def __init__(self, name, balance, checking_account):
        self.name = name
        self.balance = balance
        self.checking_account = checking_account
    def withdraw(self, money):
        if money > self.balance:
            raise ValueError
        self.balance -= money
        return f'{self.name} has {self.balance}.'
    def check(self, other_user, money):
        if other_user.balance < money or not other_user.checking_account:
            raise ValueError
        if  other_user.balance >= money:
            self.add_cash(money)
            other_user.withdraw(money)
            return f'{self.name} has {self.balance} and {other_user.name} has {other_user.balance}.'
    def add_cash(self, money):
        self.balance += money
        return f'{self.name} has {self.balance}.'
