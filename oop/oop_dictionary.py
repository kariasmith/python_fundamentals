# Making Object Instances from Dictionary Data

# Consider the following dictionary:

kevin = {"name": "Kevin Durant", "age":34, "position": "small forward", "team": "Brooklyn Nets"}

# Let's say you were receiving data from an external source like a data base, and wanted to turn this 
# dictionary data into a Player object so you could write some useful methods associated with players. 
# You can imagine just from the way the dictionary is structured that you might write your class like this:

class Player:
    def __init__(self, name, age, position, team):
        self.name = name
        self.age = age
        self.position = position
        self.team = team

# Okay, now that we have a class defined, let's take our dictionary info to make a Player instance.

kevin = {"name": "Kevin Durant", "age":34, "position": "small forward", "team": "Brooklyn Nets"}
     
# Pass in all the values from the dictionary by their keys
player_kevin = Player(kevin["name"], kevin["age"], kevin["position"], kevin["team"])
print(player_kevin.position) # prints small forward

# Now you have a Player object, that you can write methods for! You can also make more player instances 
# if you have more data that comes back in that format.

'''
Other Fun Facts About Dictionaries
They're Fast

You are already familiar with Python dictionaries, but almost every language has a built-in key-value pair data structure. They are widely used, extremely powerful and considered fundamental for one primary reason:

    They provide constant-time lookup, insertion and deletion on average

Many extremely common problems are best solved with the key-value pair data structure (commonly called a hash table in computer science.) Some examples: Dealing with uniqueness of data, frequency of values, and finding duplicates in data sets.
Also Called a Hash Table

Here are some of the names you will hear them called.
Dictionaries	Python
Objects (misleadingly!)	JavaScript, JSON
Maps, Hash Maps	Java, C++
Hash Table	C#
Associative Array	PHP
'''