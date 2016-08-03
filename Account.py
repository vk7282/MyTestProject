class Customer(object):

    def __init__(self, name, balance=0.0):
        """Return a Customer object whose name and starting balance is given."""
        self.name = name
        self.balance = balance

    def withdraw(self, amount):
        """Return the balance remaining after withdrawing amount"""

        if amount > self.balance:
            raise Exception('Amount greater than available balance.')
        self.balance -= amount
        print "Rs.",amount, " is withdrawn from your account."
        print "Total remaining balance:- ", self.balance

    def deposit(self, amount):
        """Return the balance remaining after depositing amount"""

        self.balance += amount
        print "Rs.",amount, " is deposited to your account."
        print "Total remaining balance:- ", self.balance