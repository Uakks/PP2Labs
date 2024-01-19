class Account:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def withdraw(self, amount):
        if amount > self.balance:
            print("You don't have enough")
        else:
            self.balance -= amount
            return self

    def deposit(self, amount):
        self.balance += amount