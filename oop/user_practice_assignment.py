'''
Assignment: User

For this assignment you will create the user class and add a couple methods!
Attributes:

On instantiation of a user, the following attributes should be passed in as arguments:

    first_name
    last_name
    email
    age

Also include default attributes:

    is_rewards_member - default value of False
    gold_card_points = 0

Methods:

    display_info(self) - Have this method print all of the users' details on separate lines.
    enroll(self) - Have this method change the user's member status to True and set their gold card points to 200.
    spend_points(self, amount) - have this method decrease the user's points by the amount specified.

Ninja Bonuses:

    Add logic in the enroll method to check if they are a member already, and if they are, print "User already a member." 
    and return False, otherwise return True.
    Add logic in the spend points method to be sure they have enough points to spend that amount and handle appropriately.


'''

class User:
    def __init__(self, first_name, last_name, email, age) -> None:
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.is_rewards_member = False
        self.gold_card_points = 0

def display_info(self):
    print("First Name is: ",self.first_name, "\n""Last Name is: ", self.last_name, "\n""Email: ", self.email, "\n""Reward Member? ", self.is_rewards_member, "\n""Points: ", self.gold_card_points)
# print users' details on separate lines

def enroll(self):
    if self.is_rewards_member == True:
        print("User already a member.", "\n",self.is_rewards_member)
    else:
        print(self.is_rewards_member, "Enrolling member")
        self.is_rewards_member = False
        self.gold_card_points = 200
# change status to True, gold card points to 200
# if member already, print "User already a member." and return False, otherwise return True.

def spend_points(self, amount):
    if self.gold_card_points > amount:
        print("Starting balance: ", self.gold_card_points)
        self.gold_card_points = self.gold_card_points - amount
        print("Purchase amount: ", amount)
        print("New balance: ", self.gold_card_points)
    else:
        print("Current balance not enough for purchase: ", self.gold_card_points)
# decrease the user's points by the amount
# check if they have enough points to spend that amount and handle appropriately

user_kari = User("Kari","Smith","kari@email.com",40)
# display_info(user_kari)
# enroll(user_kari)
# display_info(user_kari)
spend_points(user_kari, 50)
# spend_points(user_kari, 300)
user_alex = User("Alex","Postate","alex@email.com",30)
user_reese = User("Reese","Dono","reese@email.com",45)
enroll(user_alex)
spend_points(user_alex,80)
display_info(user_kari)
display_info(user_alex)
display_info(user_reese)