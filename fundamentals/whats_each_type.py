num1 = 42 #integer
num2 = 2.3 #float  ice cream float?  nope numerical kind
boolean = True #bollean don't think I spelled that one right lol
string = 'Hello World' #basic string
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives'] #list
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False} #dictionary we use alot of these in automation
fruit = ('blueberry', 'strawberry', 'banana') #Tuples can't be changed
print(type(fruit)) #prints out what is the type listed in the parens
print(pizza_toppings[1]) #printing out the value from the value assigned at 1 Sausage
pizza_toppings.append('Mushrooms') #adding a new value to the list
print(person['name']) #prints the value for the name field in the person dict John
person['name'] = 'George' #updating the name value in the dict
person['eye_color'] = 'blue' #hmm eye_color doesn't already exist in the dict, wonder if this will add or error out
print(fruit[2]) #prints out the value from the 2nd place in the tuple banana

if num1 > 45: #conditional if
    print("It's greater")
else:   # else
    print("It's lower")

if len(string) < 5: #a new if statement! gasp checking the length of my string, be modest!
    print("It's a short word!")
elif len(string) > 15:  #elif is else if checking the length how dare you
    print("It's a long word!")
else:   # it's the final else down *guitar plays*
    print("Just right!")
# hey I'm trying to stay awake here!
for x in range(5): #ooo a foor loop, range? hmm something else to look up
    print(x)
for x in range(2,5):
    print(x)
for x in range(2,10,3):
    print(x)
x = 0
while(x < 5): #look it's a while loop
    print(x) #0, 1, 2, 3, 4
    x += 1

pizza_toppings.pop() #pop is removing an value from a list, if no number is listed an error thrown or the whole thing *dramatic music*
pizza_toppings.pop(1) #removing the value that is in 1 spot Sausage

print(person) #print statement of the whole dictionary
person.pop('eye_color') #don't remove his eye balls nooooo!!
print(person) # printing out the dictionary again to the eye balls have been removed LOL

for topping in pizza_toppings: #floor loop of the list
    if topping == 'Pepperoni': #p_t[0] will meet this if statement
        continue #continue statement
    print('After 1st if statement') 
    if topping == 'Olives': #if statement checking for when the topping matches Olives
        break #then it will break out of the for loop

def print_hello_ten_times(): #gasp clasping the pearl necklace a definition of a function!
    for num in range(10): #for loop will run when function called, ring ring yellow?
        print('Hello')

print_hello_ten_times() #you called me right away! GASP

def print_hello_x_times(x): #how dare you define another function right after calling me and demand a parameter
    for num in range(x): #your simple for loop using the parameter
        print('Hello')

print_hello_x_times(4) #invoking the 4th amendment.....hmmm wrong number but use it anyways

def print_hello_x_or_ten_times(x = 10): #defining all those Hellos but no Sunshines to go with it...
    for num in range(x):
        print('Hello')

print_hello_x_or_ten_times() #invoking the function *queue dramatic music* it used the 10 parameter
print_hello_x_or_ten_times(4) #invoking the function and using 4 as the parameter

#Super curious if anyone ever actually reads these....  sticking my tongue out at you!
"""
Bonus section
"""

# print(num3)
# num3 = 72
# fruit[0] = 'cranberry'
# print(person['favorite_team'])
# print(pizza_toppings[7])
#   print(boolean)
# fruit.append('raspberry')
# fruit.pop(1)

num1 = 42 # variable declaration, number initialized
num2 = 2.3 # variable declaration, decimal/float initialized
boolean = True # variable declaration, boolean initialized
string = 'Hello World' # variable declaration, string initialized

# variable declaration, list initialized
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives']

# variable declaration, dictionary initialized
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False}

# variable declaration, tuple initialized
fruit = ('blueberry', 'strawberry', 'banana')
# print to console, type check
print(type(fruit))

# print to console, List access value
print(pizza_toppings[1])

#list add value
pizza_toppings.append('Mushrooms')

# print to console, Dictionary access value
print(person['name'])

# Dictionary change value
person['name'] = 'George'
# Dictionary change value
person['eye_color'] = 'blue'

# print to console, Tuple access data
print(fruit[2])

# Conditional if, evaluation, print to console, Conditional else, print to console
if num1 > 45:
    print("It's greater")
else:
    print("It's lower")

# Conditional if - elif - else, print to console.
if len(string) < 5:
    print("It's a short word!")
elif len(string) > 15:
    print("It's a long word!")
else:
    print("Just right!")

# For Loop start at 0 and goes up to until 5
for x in range(5):
    print(x)
# For Loop start at 2 and goes up to until 5
for x in range(2,5):
    print(x)
# For loop start at 2 goes up to until 10, increments by 3
for x in range(2,10,3):
    print(x)

#While Loop, variblae declaration
x = 0
while(x < 5):
    # printing to console
    print(x)
    # incrementing x
    x += 1

# List delete value at end
pizza_toppings.pop()
# list delete value at index
pizza_toppings.pop(1)

# print to console of dictionary
print(person)
# Dictionary delete value
person.pop('eye_color')
#print to console of dictionary
print(person)

# for loop through a list
for topping in pizza_toppings:
    #Conditional if
    if topping == 'Pepperoni':
        # Conintues
        continue
    # print to console
    print('After 1st if statement')
    # Conditional if
    if topping == 'Olives':
        # stops the loop
        break

# function declaration
def print_hello_ten_times():
    # for loop starts at 0 goes up until 10
    for num in range(10):
        # print to console
        print('Hello')

# Function Call
print_hello_ten_times()

# function Declaration with parameter x
def print_hello_x_times(x):
    # For loop up until a given number x
    for num in range(x):
        # print to console
        print('Hello')

# function call arguement of 4
print_hello_x_times(4)

# function declaration with default parameter
def print_hello_x_or_ten_times(x = 10):
    # For loop until x
    for num in range(x):
        # print to console
        print('Hello')

# Function call goes to 10
print_hello_x_or_ten_times()
# function call goes to 4
print_hello_x_or_ten_times(4)


"""
Bonus section
"""

# print(num3)
# num3 = 72
# fruit[0] = 'cranberry'
# print(person['favorite_team'])
# print(pizza_toppings[7])
#   print(boolean)
# fruit.append('raspberry')
# fruit.pop(1)
