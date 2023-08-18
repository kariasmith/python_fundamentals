'''Conditional statements allow us to run certain lines of code depending on whether certain 
conditions are met.  These statements control the flow of how our code is executed by the interpreter.  
In Python, the keywords for conditional statements are if, elif, and else. Here are some examples:'''

    x = 12
    if x > 50:
    	print("bigger than 50")
    else:
    	print("smaller than 50")
    # because x is not greater than 50, the second print statement is the only one that will execute
    
    x = 55
    if x > 10:
    	print("bigger than 10")
    elif x > 50:
    	print("bigger than 50")
    else:
    	print("smaller than 10")
    # even though x is greater than 10 and 50, the first true statement is the only one that will execute, so we will only see 'bigger than 10'
    
    if x < 10:
    	print("smaller than 10")
    # nothing happens, because the statement is false  

    '''
    Operator 	Description 	Example
== 	Checks if the value of two operands are equal 	1 == 2 => False
1 == 1 => True

!= 	Checks if the value of two operands are not equal 	1 != 2 => True
1 != 1 => False

> 	Checks if the value of left operand is greater than the value of right operand 	1 > 2 => False
2 > 1 => True

< 	Checks if the value of left operand is less than the value of right operand 	1 < 2 => True
2 < 1 => False

>= 	Checks if the value of left operand is greater than or equal to the value of right operand 	1 >= 2 => False
2 >= 2 => True

<= 	Checks if the value of left operand is less than or equal to the value of right operand 	1 <= 2 => True
2 <= 2 => True

and 	Checks that each expression on the left and right are both True 	(1 <= 2) and (2 <= 3) => True
(1 <= 2) and (2 >= 3) => False
(1 >= 2) and (2 >= 3) => False

or 	Checks if either the expression on the left or right is True 	(1 <= 2) or (2 >= 3) => True
(1 <= 2) or (2 <= 3) => True
(1 >= 2) or (2 >= 3) => False

not 	Reverses the true-false value of the operand 	not True => False
not False => True
not 1 >= 2 => True
not 1 <= 2 => False
not (1 <= 2 and 2 >= 3)  => True
not 1 <= 2 and 2 >= 3 => False
    '''
