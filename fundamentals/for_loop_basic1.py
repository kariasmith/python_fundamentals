"""

    Basic - Print all integers from 0 to 150.

    Multiples of Five - Print all the multiples of 5 from 5 to 1,000

    Counting, the Dojo Way - Print integers 1 to 100. If divisible by 5, print "Coding" instead. 
    If divisible by 10, print "Coding Dojo".
    (What is the Divisibility Rule of 5? The divisibility rule of 5 states that if the digit on the units place, 
    that is, the last digit of a given number is 5 or 0, then such a number is divisible by 5. 
    For example, in 39865, the last digit is 5, hence, the number is completely divisible by 5.)

    Whoa. That Sucker's Huge - Add odd integers from 0 to 500,000, and print the final sum.

    Countdown by Fours - Print positive numbers starting at 2018, counting down by fours.

    Flexible Counter - Set three variables: lowNum, highNum, mult. 
    Starting at lowNum and going through highNum, print only the integers that are a multiple of mult. 
    For example, if lowNum=2, highNum=9, and mult=3, the loop should print 3, 6, 9 (on successive lines)

"""

# Basic
for i in range(0, 151):
    print(i)

# Multiples of 5
for i in range(5, 1001, 5):
    print(i)

# Counting, the Dojo Way
for i in range(1, 101, 1):
    
    if i % 10 == 0:
        print("Coding")
    elif i % 5 == 0:
        print("Coding Dojo")
    else:
        print(i)

#  Whoa. That Sucker's Huge
final_sum = 0
for i in range(1, 500001, 2):
    
    if i % 2 == 1:
        # print(i)
        final_sum = final_sum + i

print(final_sum)

# Countdown by Fours
for i in range(2018, 0, -4):
    print(i)

# Flexible Counter
lowNum = 5
highNum = 679
mult = 9
for i in range(lowNum, highNum):
    if i%mult == 0:
        print(i)