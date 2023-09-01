'''
There is a way to call on user1 just once and keep attaching new method calls to the end of the previous one, like so:

user1.display_info().enroll().spend_points(50).display_info()
user2.enroll().spend_points(80).display_info()

This is called chaining. In order for this to work, each method must return self. By returning self, if we recall how functions work, each method call will now be equal to the instance that called it.

For example if user1.spend_points(50) returns its own instance (user1 ), then we can call one of that instance's methods after that call, like user1.spend_points(50).display_info().

class User:
    # .. constructor
    
    def display_info(self):
        # your code
    
    	# new return statement, returns this same object
        return self

The practice of having OOP return its own instance is pretty common and is done in other programming languages, though the variable name in some languages is not self, but instead this.

Note: This only works with methods that do not need to return anything. If your method needs to return something other than self, it is not possible to chain the method.
'''

class User:
    def __init__(self, first_name, last_name, email, age):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.is_rewards_member = False
        self.gold_card_points = 0

def display_info(self):
    print("First Name is: ",self.first_name, "\n""Last Name is: ", self.last_name, "\n""Email: ", self.email, "\n""Reward Member? ", self.is_rewards_member, "\n""Points: ", self.gold_card_points)
    return self
# print users' details on separate lines

def enroll(self):
    if self.is_rewards_member == True:
        print("User already a member.", "\n",self.is_rewards_member)
    else:
        print(self.is_rewards_member, "Enrolling member")
        self.is_rewards_member = False
        self.gold_card_points = 200
    return self
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
    return self
# decrease the user's points by the amount
# check if they have enough points to spend that amount and handle appropriately

user_kari = User("Kari","Smith","kari@email.com",40)
# display_info(user_kari)
# enroll(user_kari)
# display_info(user_kari)

# spend_points(user_kari, 300)
user_alex = User("Alex","Postate","alex@email.com",30)
user_reese = User("Reese","Dono","reese@email.com",45)

'''
Example they gave:
user1.display_info().enroll().spend_points(50).display_info()
user2.enroll().spend_points(80).display_info()
'''
user_kari.display_info()
# user_kari.display_info().spend_points(50).display_info()
# user_alex.display_info().enroll().spend_points(80).display_info()
# user_reese.display_info().spend_points(200).display_info()