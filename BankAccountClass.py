
# Topics: Create class BankAccount
# Formatting Output, Importing Modules
# Description: Write a basic class that simulates a bank account that supports the following options:
# 1.Customers can deposit and withdraw funds.
# 2.If sufficient funds are not available for withdrawal, a $10.00 overdraft penalty is charged.
# 3.Once within a given month, interest can be added to the account. The interest rate can vary every month.
# User Input: None


import datetime
from decimal import *
from locale import *
setlocale( LC_ALL, 'en_CA.UTF-8' )

class BankAccount:
    # class variables set here
    INITBALANCE = Decimal(0.0)
    MINIRATE = 1
    MAXIRATE = 2
    OVERDRAFT_FEES = Decimal(10.0)

    # constructor initialization
    def __init__(self, initial_balance=INITBALANCE):
        # local to instance _last_interest_date var used to determine applied date for interest
        self._last_interest_date = ''
        # setting balance default setters in __init__
        self.balance = Decimal(initial_balance) if Decimal(initial_balance) > self.INITBALANCE else self.INITBALANCE

    # deposit method
    def deposit(self, input_amount):
        input_amount = self.valid_amount(input_amount)
        self.balance = self.balance + input_amount
        return True

    # withdraw method
    def withdrawal(self, input_amount):
        input_amount = self.valid_amount(input_amount)
        if self.balance < input_amount:
            self.balance = self.balance - self.OVERDRAFT_FEES - input_amount
            return True
        else:
            self.balance = self.balance - input_amount
            return False

    # balance getter
    def get_balance(self):
        return currency(self.balance)

    # add_interest method
    def add_interest(self, rate):
        if self.validate_rate(rate) and self.balance > self.INITBALANCE:
            if not self._last_interest_date or \
                    datetime.date.today() > self._last_interest_date:
                self._last_interest_date = datetime.date.today()
                self.balance = self.balance * Decimal(1 + rate / 100)
                return True
            else:
                # return can be used to find out the next date to add interest
                return self._last_interest_date + datetime.timedelta(20)
                #return False

    # static method to validate the input_amount.
    @staticmethod
    def valid_amount(input_amount):
        if (isinstance(input_amount, float) or isinstance(input_amount, int)) \
                and input_amount > BankAccount.INITBALANCE:
            amount = Decimal(input_amount)
        else:
            amount = BankAccount.INITBALANCE
        return amount

    # class static method to validate the rate input
    @staticmethod
    def validate_rate(rate):
        try:
            if BankAccount.MINIRATE <= Decimal(rate) <= BankAccount.MAXIRATE:
                return Decimal(rate)
        except (InvalidOperation,TypeError):
            return False
            # here I am not sure do I need pass or not?
            pass



