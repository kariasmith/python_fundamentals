'''
A Dictionary is another mutable sequence type that can store any number of Python objects, including other sequence types. 
Dictionaries consist of pairs (called items) of keys and their corresponding values. 
While this data structure is known as a dictionary in Python, you'll see the same structure referred to as an 
associative array or hash table in other languages. In general, hash table is the most generic term.

The following is a general summary of the characteristics of a Python dictionary:

    A dictionary is an unordered collection of objects.
    Values are accessed using a key (typically a string).
    A dictionary can shrink or grow as needed.
    The contents of dictionaries can be modified.
    Dictionaries can be nested.
    Sequence operations such as slice cannot be used with dictionaries.
'''

#literal notation
person = {"first": "Ada", "last": "Lovelace", "age": 42, "is_organ_donor": True}
capitals = {} #create an empty dictionary

 #create an empty dictionary then add values
capitals["svk"] = "Bratislava"
capitals["deu"] = "Berlin"
capitals["dnk"] = "Copenhagen"
# my_dict["some_string"] = some_value

'''
Each key in a dictionary must be unique. 
If you make an assignment using an existing key as the index, the old value associated with that key is 
overwritten by the new value. You can use this characteristic to an advantage in order to modify an existing
 value for an existing key.
'''

person = {"first": "Ada", "last": "Lovelace", "age": 42, "is_organ_donor": True}
# Adds a new key value pair for email to person
person["email"] = "alovelace@codingdojo.com"
        
# Changes person's "last" value to "Bobada"
person["last"] = "Bobada"
print(person)

# Sometimes you may want to test if a key already exists in the dictionary to know whether to add 
# an initial value or replace an existing value.

if some_key in my_dictionary:
    # update the value

# This also works with the not logical operator:

if "email" not in person:
    person["email"] = "newemail@email.com"
else:
    print("Would you like to replace your existing email?")

# Accessing Values

# To access the values of a dictionary, you can use the familiar square brackets along with the key to obtain its value.

print(person["first_name"])
full_name = person["first_name"] + " " + person["last_name"]

# Removing Values

# There are 2 ways to remove a key:value pair from a dictionary. 

value_removed = capitals.pop('svk') # will remove the key 'svk' and return it's value
del capitals['dnk'] # will delete the key, and not return anything

# Multi-Line Syntax Too!

# You can write any dictionary's key-value pairs on multiple lines to make it easier to read, which is very useful for larger dictionaries. For example the following dictionary..

person = {"first": "Ada", "last": "Lovelace", "age": 42, "is_organ_donor": True}

# ..can also be written like so:

person = {
    "first": "Ada", 
    "last": "Lovelace", 
    "age": 42, 
    "is_organ_donor": True
}

'''
Python includes the following standalone functions for dictionaries:

    len() - give the total length of the dictionary.
    str() - produces a string representation of a dictionary.
    type() - returns the type of the passed variable. If passed variable is a dictionary, it will then return a dict type.

Here are some very useful Python dictionary methods:

    .clear() - removes all elements from the dictionary
    .get(key, default=None) - A safe way to get a value, if the key might not exist. Returns the value for the specified key or None (or a value you specify) if the key is not in the dictionary.
    .update(pairs_to_update) - Add and update multiple key-value pairs at once, by passing in another dictionary of the pairs to update and add.
https://www.w3schools.com/python/python_ref_dictionary.asp
'''

# Dictionaries are also iterable. When we iterate through a dictionary, the iterator is each of the keys of the dictionary.

my_dict = { "name": "Noelle", "language": "Python" }
for each_key in my_dict:
    print(each_key)
# output: name, language

# That means if we want the values of our dictionary, we might do something like this:

my_dict = { "name": "Noelle", "language": "Python" }
for each_key in my_dict:
    print(my_dict[each_key])
# output: Noelle, Python

# Dictionaries also have a few additional methods that allow us to iterate through them and have the keys 
# and/or values as the iterator. Test these out to get a better understanding:

capitals = {"Washington":"Olympia","California":"Sacramento","Idaho":"Boise","Illinois":"Springfield","Texas":"Austin","Oklahoma":"Oklahoma City","Virginia":"Richmond"}
# another way to iterate through the keys
for key in capitals.keys():
     print(key)
# output: Washington, California, Idaho, Illinois, Texas, Oklahoma, Virginia
#to iterate through the values
for val in capitals.values():
     print(val)
# output: Olympia, Sacramento, Boise, Springfield, Austin, Oklahoma City, Richmond
#to iterate through both keys and values
for key, val in capitals.items():
     print(key, " = ", val)
# output: Washington = Olympia, California = Sacramento, Idaho = Boise, etc

# Nesting is also allowed in dictionaries. In other words, dictionaries may contain lists and tuples as 
# well as other dictionaries. Likewise, lists may contain dictionaries. All of these may be many levels deep! 
# In this module you'll become more familiar with how to manipulate nested lists and dictionaries.

# List of dictionaries
users = [
    {"first": "Ada", "last": "Lovelace"}, # index 0
    {"first": "Alan", "last": "Turing"}, # index 1
    {"first": "Eric", "last": "Idle"} # index 2
]
# Dictionary of lists
resume_data = {
    #        	     0           1           2
    "skills": ["front-end", "back-end", "database"],
    #                0           1
    "languages": ["Python", "JavaScript"],
    #                0              1
    "hobbies":["rock climbing", "knitting"]
}

# Accessing Values in Nested Dictionaries

# To access a value in a nested data structure take a look at how you would access the first user's last name. 

print(users[0]["last"]) # prints Lovelace
print(resume_data["skills"][1])
print(users[2]["first"])

'''
Tip: Pay very close attention to which kind of brackets you're looking at in the nested structure. 
If it starts with {, it's the start of a dictionary and you'll need a key, to access something one level 
further into it. If it starts with [, it's a list, and you'll need an index to go one level further into it.
'''