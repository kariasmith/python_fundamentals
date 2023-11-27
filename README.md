# python_fundamentals
Mostly notes from learning python basics.

I take notes through each section and create python files. 
Some files can run without issues and some won't because those were mostly for note taking purposes.

If you have some additions or analogies that might help keep a section or idea clear. Please share!

https://docs.python.org/3/tutorial/datastructures.html

https://docs.python.org/2/library/functions.html#range

https://docs.python.org/3/library/stdtypes.html#common-sequence-operations

https://docs.python.org/3/tutorial/datastructures.html#tuples-and-sequences

Article on Modulo (what we are currently using) from Real Python: https://realpython.com/python-modulo-operator/


Why do we call it a dictionary? Think of how a classical dictionary has a word and a definition. Here, the word is the “key” you search for and the definition is the value (the meaning of that word or its human-given value).

Couple different ways to describe the brackets we see in code but I generally think of them like this:
[ ] = square brackets
{ } = curly brackets (informally called by TAs as “curly boys”
( ) = parentheses

item[“shape”] = “circle”


When we are looping, i or whatever variable we choose to call it is known as the “iterator” - which is why it commonly is written as i

Diagram of a function:
Function header —>
Function declaration (def), function name (my_function), colon (:) - needed in Python to show the following lines will be the function body (this along with indentation determine the function “scope”)

Function body —>
You can write any Python code you want in here

Function return (optional) —>
Sometimes you’ll need to use this and sometimes not; simply write “return” plus a variable or some logic

Function call (optional but needed to run code) —>
This comes after the function and needs to be at the beginning of the line (not indented) generally

When using snake and then don't switch to camel.
Great question! So this is a convention but not a rule. It will work just fine but usually best to follow the convention

And just a side note, don’t get too caught up in making your code extremely DRY (not repeating yourself) as a beginner. You will probably repeat yourself a lot and that’s okay. Over time, you will learn how to make your code more DRY. You can revisit your code and try to make it more DRY later. Functions are an easy way to do this as a beginner though.

Example:

Def my_function( parameters go here ):
   Some logic
   Return my_variable

my_function(arguments go here)

With returns we can store their values in variables
Those variables get stored in memory
Prints don’t get stored but go “poof” after they print to the console. Never stored in memory

To those who want to use the debugger, its the plugin on the left side of VS code - the one that looks like a play button with a bug
