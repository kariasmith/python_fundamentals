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
