# SWDV-630: Object-Oriented Coding
# Kyle Anderson
# Week 2 Assignment

##################################
# Driver Application
##################################
from CheckingAccount import CheckingAccount

# customer variables
customerName = 'Kyle Anderson'
customerAddress = '123 Main Street'
accountNumber = 123456
initialBalance = 1000

# some convenient driver functions defined here to prevent re-use
def printSeparator():
    print(40 * '-')

def printNewBalance(accountObj):
    print('New account balance: ${:.2f}'.format(accountObj.getBalance()))


def deposit(account, amount):
    if account.deposit(amount):
        print('Deposit made successfully')
        printNewBalance(account)
    else:
        print('Deposit failed')


def withdraw(account, amount):
    if account.withdraw(amount):
        print('Withdraw made successfully')
        printNewBalance(account)
    else:
        print('Withdraw failed')


printSeparator()
print('Checking Account Driver App')
printSeparator()

##################################
# Create our CheckingAccount object
##################################
myAccount = CheckingAccount(
    customerName, customerAddress, accountNumber, initialBalance)

print('Account created successfully.')

myAccount.printAccountDetails()

printSeparator()

##################################
# Attempt some deposits
##################################
print('Depositing $100 into checking account...')

deposit(myAccount, 100.00)

printSeparator()

print('Attempting to deposit an invalid amount into account...')

deposit(myAccount, 'abc')

printSeparator()

##################################
# Attempt some withdraws
##################################
print('Attempting to withdraw $1.23 from checking account...')

withdraw(myAccount, 1.23)

printSeparator()

print('Attempting to withdraw an invalid amount from checking account...')

withdraw(myAccount, 'abc')

printSeparator()

print('Attempting to overdraft checking account...')

withdraw(myAccount, 99999.99)

printSeparator()

##################################
# Final account details
##################################
print('Final account details:')

myAccount.printAccountDetails()
