
class BankAccount:
    
    def __init__(self, int_rate, balance): 
        self.int_rate = int_rate
        self.balance = balance

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


class User:

    def __init__(self, name) -> None:
        self.name = name
        self.account_1 = BankAccount(int_rate=0.02, balance=0)

    def make_deposit(self, amount):
        self.account_1.deposit(amount)
        #self.account_2.deposit(400.00)
        return self

    def make_withdrawal(self, amount):
        self.account_1.withdraw(amount)
        return self

    def display_user_balance(self):
        self.account_1.display_account_info()
        #print(self.account_1.balance)
        return self

#SENSEI BONUS: Allow a user to have multiple accounts; update methods so the user has to specify which account they are withdrawing or depositing to
#SENPAI BONUS: Add a transfer_money(self, amount, other_user) method to the user class that takes an amount and a different User instance, and transfers money from the user's account into another user's account.


user_kari = User("Kari")
user_kari.make_deposit(200.00).make_deposit(450.00).make_withdrawal(100).display_user_balance()
#print(user_kari.account_1.balance)