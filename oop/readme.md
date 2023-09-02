Would it surprise you to know that you have been taking advantage of OOP already? 
This grouping, or encapsulating, of properties and functionalities by object is a fundamental principle of OOP and is implemented with classes.
Whenever we declare a variable, we are creating an instance of a class. For example, by declaring x = [1,2,3], x is an instance of a list. An instance is simply an object that follows the pattern defined by its class.

Here's the syntax for creating a class that we want to call User:
class User:
    pass    # we'll fill this in shortly
And here's how we create a new instance of our class:
michael = User()
anna = User()
Over the next few tabs, we'll start fleshing out our classes with:
	•	Attributes: Characteristics shared by all instances of the class type.
	•	Methods: Actions that an object can perform. A user in a banking application, for example, may need to be able to calculate age based on the user's birthday or open a new bank account associated with that user.
