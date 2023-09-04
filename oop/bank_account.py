'''
The BankAccount class should have a balance. When a new BankAccount instance is created, 
if an amount is given, the balance of the account should initially be set to that amount; 
otherwise, the balance should start at $0. The account should also have an interest rate in decimal format. 
For example, a 1% interest rate would be saved as 0.01. The interest rate should be provided upon instantiation. 
(Hint: when using default values in parameters, the order of parameters matters!)

The class should also have the following methods:

    deposit(self, amount) - increases the account balance by the given amount
    withdraw(self, amount) - decreases the account balance by the given amount if there are sufficient funds; 
    if there is not enough money, print a message "Insufficient funds: Charging a $5 fee" and deduct $5
    display_account_info(self) - print to the console: eg. "Balance: $100"
    yield_interest(self) - increases the account balance by the current balance * the interest rate (as long as 
    the balance is positive)

'''
class BankAccount:
    
    def __init__(self, int_rate, balance): 
        self.int_rate = 0.02
        self.balance = 0
        
    def deposit(self, amount):
        print("Previous balance: ", self.balance)
        self.balance = self.balance + amount
        print("New balance: ", self.balance)
        return self

    def withdraw(self, amount):
        print("Previous balance: ", self.balance)
        if self.balance < amount:
            print("Insufficient funds: Charging a $5 fee")
            self.balance = self.balance - 5
            self.balance = self.balance - amount
            print("New balance: ", self.balance)
        else:
            self.balance = self.balance - amount
            print("New balance: ", self.balance)
        return self
        
    def display_account_info(self):
        print("Balance: $", self.balance)
        return self

    def yield_interest(self):
        print("Previous balance: ", self.balance)
        self.balance = self.balance + (self.balance * self.int_rate)
        print("New balance: ", self.balance)
        return self

account_1 = BankAccount(0.02,0.00)
account_2 = BankAccount(0.01,50.00)
# make 3 deposits and 1 withdrawal, then yield interest and display the account's info all in one line of code (i.e. chaining)
# make 2 deposits and 4 withdrawals, then yield interest and display the account's info all in one line of code (i.e. chaining)
# BONUS: use a classmethod to print all instances of a Bank Account's info
account_1.deposit(200.00).deposit(50.00).deposit(400.00).withdraw(450.00).yield_interest().display_account_info()
account_2.deposit(400.00).deposit(350.00).withdraw(40.00).withdraw(40.00).withdraw(40.00).withdraw(40.00).yield_interest().display_account_info()