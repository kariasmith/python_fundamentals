Would it surprise you to know that you have been taking advantage of OOP already? For example, you know that you can call the append method if you're working with a list, but not with a dictionary or a number. You know that you can get the length of a list or dictionary, but not of a boolean. That is because each type of thing, or object, has specific properties and functionality associated with it.
This grouping, or encapsulating, of properties and functionalities by object is a fundamental principle of OOP and is implemented with classes.
Whenever we declare a variable, we are creating an instance of a class. For example, by declaring x = [1,2,3], x is an instance of a list. An instance is simply an object that follows the pattern defined by its class.

"We need to start thinking about classes as blueprints for our custom objects. They aren't the actual objects, but a plan for what properties and functionalities they may have.  We can now create custom objects to suit the need of our web applications!"
Let's consider an example of a custom class we'll need in the context of a banking application.  As almost all applications revolve around users, they should define a User class.  The information we need about a user would be different than what we would need if we were building a social media application. Instead of allowing a user to define their own properties, we set a standard for what a user should have on our website.  This ensures consistent creation of User instances.

Here's the syntax for creating a class that we want to call User:
class User:
    pass    # we'll fill this in shortly
And here's how we create a new instance of our class:
michael = User()
anna = User()
Over the next few tabs, we'll start fleshing out our classes with:
	•	Attributes: Characteristics shared by all instances of the class type.
	•	Methods: Actions that an object can perform. A user in a banking application, for example, may need to be able to calculate age based on the user's birthday or open a new bank account associated with that user.
	•	
	•	Students will be able to articulate what a constructor (__init__ method) is used for
	•	Students will identify any line of code and syntax that calls the __init__ method
	•	Students will create an object instance of a class.
	•	Students will recognize a class definition vs the outer or global scope.
	•	Students will be able to explain what self is used for.

