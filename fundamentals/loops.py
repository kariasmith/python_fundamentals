# Loops
'''We can use Python's range function in conjunction with python for loops to repeat the same code many 
times with a number, usually called i that represents an integer that changes. This is similar to for 
loops in other languages, but the syntax is a bit different. The range() function can have between 
1 and 3 arguments and creates a sequence of integers called a range object. We primarily use this for 
creating loops that have a defined starting point and a stopping point for a sequence of integers.

I like to think of this built in range() function as having the three S’es or “start, stop, step.” Easy to remember
'''

for i in range(5):
    print(i)

'''
    i starts at 0 by default
    exits loop when i is 5 (prints 4 but not 5!)
    i increases by 1 each time by default
'''

for i in range(2, 7):
    print(i)

'''
    i starts at 2
    exits when i is 7 (prints 6 but not 7!)
    i increases by 1 each time by default
'''

for i in range(2, 16, 3):
    print(i)

'''
    i starts at 2
    exits when i is 16 or larger than 16
    i increases by 3 each time
'''

'''
Note that if you need to specify an increment other than +1, all three arguments are required. 
You may also start at a large number and go down! To decrement (think going backwards) the step 
will be a negative number to indicate i will get smaller each iteration.'''

for x in range(0, 10, 2):
    print(x)
# output: 0, 2, 4, 6, 8
for x in range(5, 1, -3):
    print(x)
# output: 5, 2

# Looping Over Lists & Strings

# FOR
for x in 'Hello':
    print(x)
# output: 'H', 'e', 'l', 'l', 'o'

my_list = ["abc", 123, "xyz"]
for i in range(0, len(my_list)):
    print(i, my_list[i])
# output: 0 abc, 1 123, 2 xyz
    
# OR 
    
for v in my_list:
    print(v)
# output: abc, 123, xyz

# While Loops
# While loops are another way of looping while a certain condition is true.
count = 0
while count <= 5:
    print("looping - ", count)
    count += 1

while <expression>:
    # do something, including progress towards making the expression False. Otherwise we'll never get out of here!

y = 3
while y > 0:
    print(y)
    y = y - 1
else:
    print("Final else statement")

'''Note that this else code section is only executed if the while loop runs normally and its conditional 
is false (whether we never entered the while loop, or we did but eventually the conditional changed from 
true to false). If instead our while loop is exited prematurely because of a break or return statement, 
then the else code section will never be executed.
'''

"""
Loop Control

We were introduced to control flow in the previous tabs with if and else statements. Loops, breaks, and continues are all a part of control flow as well. Control flow is the cornerstone of most programming languages.

When you want finer control over your loops, use the following statements to do so.
Break

The break statement exits the current loop prematurely, resuming execution at the first post-loop statement. The break statement can be used in both while and for loops.

The most common use for the break is when some external condition is triggered, requiring a hasty exit from a loop.

When loops are nested, a break will only exit from the innermost loop.
"""
for val in "string":
    if val == "i":
        break
    print(val)
# output: s, t, r

"""
Continue

The continue statement immediately returns control to the beginning of the loop. In other words, the continue statement rejects, or skips, all the remaining statements in the current iteration of the loop, and continues normal execution at the top of the loop.

The continue statement is very useful when you want to skip specific iteration(s), but still keep looping to the end.
"""
for val in "string":
    if val == "i":
        continue
    print(val)
# output: s, t, r, n, g
# notice, no i in the output, but the loop continued after the i

y = 3
while y > 0:
    print(y)
    y = y - 1
    if y == 0:
        break
else:		# only executes on a clean exit from the while loop (i.e. not a break)
   print("Final else statement")
# output: 3, 2, 1
