'''

    Countdown - Create a function that accepts a number as an input. 
    Return a new list that counts down by one, from the number (as the 0th element) down to 0 (as the last element).
        Example: countdown(5) should return [5,4,3,2,1,0]

    Print and Return - Create a function that will receive a list with two numbers. 
    Print the first value and return the second.
        Example: print_and_return([1,2]) should print 1 and return 2

    First Plus Length - Create a function that accepts a list and returns the sum of the first value in the list plus 
    the list's length.
        Example: first_plus_length([1,2,3,4,5]) should return 6 (first value: 1 + length: 5)

    Values Greater than Second - Write a function that accepts a list and creates a new list containing only the values 
    from the original list that are greater than its 2nd value. Print how many values this is and then return the new list. 
    If the list has less than 2 elements, have the function return False
        Example: values_greater_than_second([5,2,3,2,1,4]) should print 3 and return [5,3,4]
        Example: values_greater_than_second([3]) should return False

    This Length, That Value - Write a function that accepts two integers as parameters: size and value. 
    The function should create and return a list whose length is equal to the given size, and whose values
      are all the given value.
        Example: length_and_value(4,7) should return [7,7,7,7]
        Example: length_and_value(6,2) should return [2,2,2,2,2,2]

'''
'''~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'''
'''This one is working Kari.~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'''
## countdown(5) should return [5,4,3,2,1,0]
new_list = []
# def countdown(5):
# SyntaxError: invalid syntax
def countdown(x = 5):
    
    for i in range(x, -1, -1):
        #print(i)
        new_list.append(i)
    print(new_list)
    return new_list

#print(countdown())
countdown()
'''~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'''
'''This one is working Kari.~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'''

def print_and_return(x=[1,2]):
     print(x[0])
     return x[1]

print_and_return([3,5])

'''~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'''
'''This one is working Kari.~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'''
def first_plus_length(x=[]):
     # should return 6 (first value: 1 + length: 5)
     #print(x)
     length = len(x)
     #print(length)
     #print(x[0])
     print(length + x[0])
     return(length + x[0])

first_plus_length([1,2,3,4,5])

'''~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'''
'''This one is working Kari.~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'''
'''Need to fix the empty [] and 0 returning for False.~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'''

def values_greater_than_second(x=[]):
     #should print 3 and return [5,3,4]
     #[3]) should return False
     #print(x)
     nb_list=[]
     lth=len(x)
     count=0
     if (len(x)<2):
        print(False)
     else:
     #print(x[1])
        for v in x:
            #print(v)
            if v>x[1]:
                nb_list.append(v)
                count=count+1
     print(nb_list)
     print(count)

values_greater_than_second([5,2,3,2,1,4])
values_greater_than_second([1,2,3,4,5,6])
values_greater_than_second([15,2,3,2,1,4])
values_greater_than_second([3])

'''~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'''
'''This one is working Kari.~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'''

# length_and_value(4,7) should return [7,7,7,7]
# length_and_value(6,2) should return [2,2,2,2,2,2]
new_list=[]
def length_and_value(num1, num2):
    for i in range(num1,0,-1):
        new_list.append(num2)
    return new_list

print(length_and_value(4,7))
new_list=[]
print(length_and_value(6,2))