# SWDV-630: Object-Oriented Coding
# Kyle Anderson
# Week 2 Assignment

##################################
# INSTRUCTIONS
##################################
# Your assignment this week you will build a CheckingAccount class and associated driver application.  The class should contain appropriate attributes that you would find in a normal checking account:  name, address, accounts number, balance, etc

# The balance should be "private" to the class since it should only be changed through appropriate debit/credit methods.  Recall, you can simulate the private aspect using the _ character at the start of the variable name.

# The class should be saved in a file called CheckingAccount.py

# Build a driver application that instantiates a CheckingAccount object and performs a variety of debits and credits as well as prints the balance as appropriate.


class CheckingAccount:
    def __init__(self, Name="", Address="", AccountNumber="", Balance=0.00):
        super().__init__()
        self.Name = Name
        self.Address = Address
        self.AccountNumber = AccountNumber
        self.__Balance = Balance

    def getBalance(self):
        return self.__Balance

    def deposit(self, amount):
        try:
            self.__Balance += amount
            return True
        except:
            return False

    def withdraw(self, amount):
        try:
            # prevent overdrafting account
            if self.__Balance > amount:
                self.__Balance -= amount
                return True
            else:
                return False
        except:
            return False

    def printAccountDetails(self):
        # print all of the attributes and values for the object
        # this method won't require any modification as attributes are added/removed from the class
        for attribute in self.__dict__:
            print('%s: %s' % (attribute, self.__dict__[attribute]))
