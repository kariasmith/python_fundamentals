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
