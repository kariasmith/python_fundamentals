# Here's a basic example of a function:
def add(a,b):	# function name: 'add', parameters: a and b
    x = a + b	# process
    return x	# return value: x

'''
We define the input of functions using parameters. Functions can have as many parameters as we need, including 0. 
Here we've defined the say_hi function with one parameter called name:
Now, we can invoke this function by calling its name and passing in the correct number of arguments:
Wait, but what's the difference between a parameter and an argument? These two words get mixed up a lot in programming. 
In this example 'name' is a parameter while "Michael", "Anna", and "Eli", are arguments. 
We define parameters. We pass in arguments into functions.
'''

def say_hi(name):
    print("Hi, " + name)

# invoking the function 3 times, passing in one argument each time
say_hi('Michael')
say_hi('Anna')
say_hi('Eli')

# It is very important to remember the following: a function call is equal to whatever that function returns. 
# This might not make sense until we see it in action.

def say_hi(name):
    return "Hi " + name
greeting = say_hi("Michael") # the returned value from say_hi function gets assigned to the 'greeting' variable
print(greeting) # this will output 'Hi Michael'

'''
Returning a value from a function allows us to store that value in a variable. 
In this example, we invoked the say_hi function with "Michael" and set it to the greeting variable. 
When we print greeting we see that it contains the returned value of the say_hi function - "Hi Michael".

    Saving values: When you print something with  print(), strictly speaking, it doesn't have any affect on your program. 
    No data is saved or changed or passed anywhere else in the program. Print statements are primarily used for programmers to debug the code, 
    to see what's happening in the program. On the other hand, a return statement may pass a value back to the outer scope after it's done running for the program to use!
    
    Exiting the function: Reaching a return statement always means "EXIT THIS FUNCTION NOW" whether or not there is more code. 
    Any remaining code will not be run.
'''

# set defaults when declaring the parameters
def be_cheerful(name='', repeat=2):
	print(f"good morning {name}\n" * repeat)
be_cheerful()    # output: good morning (repeated on 2 lines)
be_cheerful("tim")    # output: good morning tim (repeated on 2 lines)
be_cheerful(name="john")    # output: good morning john (repeated on 2 lines)
be_cheerful(repeat=6)    # output: good morning (repeated on 6 lines)
be_cheerful(name="michael", repeat=5)    # output: good morning michael (repeated on 5 lines)
# NOTE: argument order doesn't matter if we are explicit when sending in our arguments!
be_cheerful(repeat=3, name="kb")    # output: good morning kb (repeated on 3 lines)

'''

    no arguments are provided -- the defaults are used
    one unnamed argument provided -- provided value is used as the value for the first parameter, and the second parameter's default value is used
    one named argument provided -- provided value is used as the value of the parameter of the same name, and the other parameter's default value is used
    both unnamed arguments provided -- values assigned to parameters in order (i.e. what we've been doing up to this point)
    both named arguments provided -- values are assigned to associated parameter (and then order doesn't matter!)

'''

def multiply(num_list, num):
    for x in num_list:
        x *= num
    return num_list
a = [2,4,10,16]
b = multiply(a,5)
print(b)
# output:
# >>>[2,4,10,16]

'''
  def multiply(num_list, num): #don't go inside the function until the function is called
  a = [2,4,10,16]
  b = multiply(a,5) # now our function executes; what is a function call equal to?
  print(b) # and the resulting value is printed
'''

# Now comes the first unknown. Ask yourself what is your input, and what do you expect as output. 
# If you get unexpected results, you should work to eliminate all unknowns. 
# Try inserting a print statement as the first line. 
# Sometimes it's useful to insert a print just to be sure code is executing when we think it is, 
# but more often we can get more information by displaying some data we've passed into our function. 
# Our code should now look like this:

def multiply(num_list, num):
    print(num_list, num)
    inbow">for x in num_list:
        x *= num
    return num_list
a = [2,4,10,16]
b = multiply(a,5)
print(b)
# output:
>>>[2,4,10,16] 5
>>>[2,4,10,16]

# Our output confirms that our code is doing everything we've tested for so far. 
# Now to prove that our next line runs as expected. 
# This line: for x in num_list: indicates the start of a for loop. 
# Let's confirm we're entering the loop, and that "x" contains the value we expect. 
# Now our code looks like this:

def multiply(num_list,num):
    print(num_list, num)
    for x in num_list:
        print(x)
        x *= num
    return num_list
a = [2,4,10,16]
b = multiply(a,5)
print(b)
# output:
>>>[2, 4, 10, 16] 5
>>>2
>>>4
>>>10
>>>16
>>>[2, 4, 10, 16]

# Now we know the loop is completing as expected and that, as our loop runs, x is equal to every 
# value in the list in sequence. Now it gets a little more complicated. What should we ask ourselves next? 
# Knowing what is the most useful thing to print is a skill you will acquire over time. Next, 
# let's check if we're successfully changing our x value.

def multiply(num_list,num):
    print(num_list, num) # output should be [2,4,10,16] 5
    for x in num_list:
        print(x)
        x *= num
        print(x)
    return num_list
a = [2,4,10,16]
b = multiply(a,5)
print(b)
# output:
>>>[2,4,10,16] 5
>>>2
>>>10
>>>4
>>>20
>>>10
>>>50
>>>16
>>>80
>>>[2, 4, 10, 16]

def multiply(num_list,num):
    print(num_list, num) # output should be [2,4,10,16] 5
    for x in num_list:
        print(x)
        x *= num
        print(num_list)
    return num_list
a = [2,4,10,16]
b = multiply(a,5)
print(b)
# output:
>>>[2, 4, 10, 16] 5
>>>2
>>>[2, 4, 10, 16]
>>>4
>>>[2, 4, 10, 16]
>>>10
>>>[2, 4, 10, 16]
>>>16
>>>[2, 4, 10, 16]

# Aha! Here's some unexpected output. Now we know how to use print statements to find out where a 
# problem is occurring. Once we've discovered that, we can make an educated guess as to what we 
# should be searching. Formulating a good search is a skill best learned by trial and error. 
# Try searching "unable to modify list value in for loop python"

def multiply(num_list,num):
    for x in range(len(num_list)):
        num_list[x] *= num
    return num_list
a = [2,4,10,16]
b = multiply(a,5)
print(b)
# output:
>>>[10,20,50,80]