# Boolean Values - Assesses the truth value of something. It has only two values: True and False (note the uppercase T and F)
is_hungry = True
has_freckles = False

# Numbers - Integers (whole numbers), floating point numbers (commonly known as decimal numbers), and complex numbers
age = 35 # storing an int
weight = 160.57 # storing a float

# Strings - literal text
name = "Joe Blue"

# Composite types
# Tuples - A type of data that is immutable (can't be modified after its creation) and can hold a group of values. 
# Tuples can contain mixed data types.
dog = ('Bruce', 'cocker spaniel', 19, False)
print(dog[0])		# output: Bruce
dog[1] = 'dachshund'	# ERROR: cannot be modified ('tuple' object does not support item assignment)

# Lists - A type of data that is mutable and can hold a group of values. Usually meant to store a collection of related data.
empty_list = []
ninjas = ['Rozen', 'KB', 'Oliver']
print(ninjas[2]) 	# output: Oliver
ninjas[0] = 'Francis'
ninjas.append('Michael')
print(ninjas)	# output: ['Francis', 'KB', 'Oliver', 'Michael']
ninjas.pop()
print(ninjas)	# output: ['Francis', 'KB', 'Oliver']
ninjas.pop(1)
print(ninjas)	# output: ['Francis', 'Oliver']

# Dictionaries - A group of key-value pairs. Dictionary elements are indexed by unique keys which are used to access values. 
# When you're ready, you can find more built-in dictionary methods
# https://www.w3schools.com/python/python_ref_dictionary.asp
empty_dict = {}
new_person = {'name': 'John', 'age': 38, 'weight': 160.2, 'has_glasses': False}
new_person['name'] = 'Jack'	# updates if the key exists, adds a key-value pair if it doesn't
new_person['hobbies'] = ['climbing', 'coding']
print(new_person)	
# output: {'name': 'Jack', 'age': 38, 'weight': 160.2, 'has_glasses': False, 'hobbies': ['climbing', 'coding']}
w = new_person.pop('weight')	# removes the specified key and returns the value
print(w)		# output: 160.2
print(new_person)	
# output: {'name': 'Jack', 'age': 38, 'has_glasses': False, 'hobbies': ['climbing', 'coding']}   

# If we're ever unsure of a value or variable's data type, we can use the type function to find out. For example:
print(type(2.63))		# output: <class 'float'>
print(type(new_person))		# output: <class 'dict'>

# For data types that have a length attribute (eg. lists, dictionaries, tuples, strings), we can use the len function to get the length:
print(len(new_person))		# output: 4 (the number of key-value pairs)
print(len('Coding Dojo'))	# output: 11 

#Numbers 
'''     int - whole numbers, positive or negative.  ex. 35
    float - decimal numbers, positive or negative.  ex. 4.2
    complex - are a part of the real number system and are often referenced with the letter j.  ex. 1 + 3j.  
    **Note** If you're not sure if you need to use them, it's safe to say you can ignore this data type.'''
print(type(24))
print(type(3.9))
print(type(3j))

# All Python objects have data type methods we can use to convert number types from one to another.
int_to_float = float(35)
float_to_int = int(44.2)
int_to_complex = complex(35)
print(int_to_float)
print(float_to_int)
print(int_to_complex)
print(type(int_to_float))
print(type(float_to_int))
print(type(int_to_complex))
