# Topics: Create module to test BankAccount class
# Formatting Output, Importing Modules
# Description: Test Run Requirements: Provide a test driver that includes at minimum the following actions:
# -Instantiate a bank account with an original balance of $1000.00
# -Deposit $500.00
# -Withdraws $2000.00
# -Adds 1% interest
# -Adds  2% interest
# -Deposit $125,000.99
# -Withdraws $0.99
# -Withdraws $126,500.00
# -Withdraws $10.00
# -Adds 1% interest
# Show the account balance after each action.
#  User Input: None
# Output: results as per lab spec.
# Development Environment:  MAC home


from BankAccountClass import BankAccount

def main():
    # Instantiate a bank account with an original balance of $1000.00
    myBank = BankAccount('1000.00')
    print("Deposited $1000. Remaining Balance: ", myBank.get_balance())
    myBank.deposit('fsfsdf')
    print("Deposited fsfdf. Remaining Balance: ", myBank.get_balance())
    # Deposit $500.00
    myBank.deposit(500.00)
    print("Deposited $500 ", myBank.get_balance())

    myBank.add_interest(2)
    print("Added 2% interest. Remaining Balance: ", myBank.get_balance())
    second_time = myBank.add_interest(1)
    print("Try to add 1% interest second time this month. Cant add interest, n/a until", second_time,
          "\nRemaining Balance is still ", myBank.get_balance() )

    # Withdraws $2000.00
    balance = myBank.withdrawal('2000.00')
    print("Withdraw $2000. Remaining Balance: ", myBank.get_balance())
    # # Adds 1% interest
    myBank.add_interest(1)
    print("Added 1% interest. Remaining Balance: ", myBank.get_balance())
    # # Adds  2% interest
    myBank.add_interest(2)
    print("Added 2% interest. Remaining Balance: ", myBank.get_balance())
    # # Deposit $125,000.99
    myBank.deposit('125,000.99')
    print("Deposited $125,000,99. Remaining Balance: ", myBank.get_balance())
    # # Withdraws $0.99
    myBank.withdrawal(0.99)
    print("Withdraw $0.99. Remaining Balance: ", myBank.get_balance())
    # Withdraws $126,500.00
    myBank.withdrawal(126500)
    print("Withdraw $126,500.00. Remaining Balance: ", myBank.get_balance())
    # Withdraws $10.00
    myBank.withdrawal(10.00)
    print("Withdraw $10. Remaining Balance: ", myBank.get_balance())
    # Adds 1% interest
    myBank.add_interest(1)
    print("Added 1% interest. Remaining Balance: ", myBank.get_balance())


'''Deposited $1000. Remaining Balance:  $1000.00
Deposited fsfdf. Remaining Balance:  $1000.00
Deposited $500  $1500.00
Added 2% interest. Remaining Balance:  $1530.00
Try to add 1% interest second time this month. Cant add interest, n/a until 2018-11-05 
Remaining Balance is still  $1530.00
Withdraw $2000. Remaining Balance:  $1530.00
Added 1% interest. Remaining Balance:  $1530.00
Added 2% interest. Remaining Balance:  $1530.00
Deposited $125,000,99. Remaining Balance:  $1530.00
Withdraw $0.99. Remaining Balance:  $1529.01
Withdraw $126,500.00. Remaining Balance:  -$124980.99
Withdraw $10. Remaining Balance:  -$125000.99
Added 1% interest. Remaining Balance:  -$125000.99

Process finished with exit code 0'''