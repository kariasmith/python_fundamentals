
fruits = ['apple', 'banana', 'orange', 'strawberry']
vegetables = ['lettuce', 'cucumber', 'carrots']
fruits_and_vegetables = fruits + vegetables
print(fruits_and_vegetables)
salad = 3 * vegetables
print(salad)


drawers = ["documents", "envelopes", "pens"]
    
# access the drawer with index of 0 and print value
print(drawers[0])  #prints documents
# access the drawer with index of 1 and print value
print(drawers[1]) #prints envelopes
# access the drawer with index of 2 and print value
print(drawers[2]) #prints pens
    
# replace "documents" with "tchotchkes"
drawers[0] = "tchotchkes"
print(drawers) # prints ["tchotchkes", "envelopes", "pens"]
    
# stores the value "tchotchkes" in a temporary variable.
top_contents = drawers[0]
    
# Replaces the value at index 1
# with whatever value is stored at index 0
drawers[1] = drawers[0]
print(drawers) # prints ["tchotchkes", "tchotchkes", "pens"]

nums = [1,2,3,4,5]
nums.append(99)
print(nums)
#the output would be [1,2,3,4,5,99]

words = ["start","going","till","the","end"]
# Sub-ranges (portions) of the list
print(words[1:]) # prints ['going', 'till', 'the', 'end']
print(words[:4]) # prints ['start', 'going', 'till', 'the']
print(words[2:4]) # prints ['till', 'the']
    
# Making a copy of a list
copy_of_words = words[:]
copy_of_words.append("dojo") # only appends to the copy
print(copy_of_words) # prints ['start', 'going', 'till', 'the', 'end', 'dojo']
print(words) # prints ['start', 'going', 'till', 'the', 'end']

#https://docs.python.org/3/library/stdtypes.html#common-sequence-operations

# Built-in Python Functions for Sequences

    len(sequence) #returns the length (number of items) in a sequence.
    max(sequence) #returns the highest value in a sequence.
    min(sequence) #returns the lowest value in a sequence.
    sorted(sequence) #returns a sorted sequence
# https://docs.python.org/3/library/functions.html

# List-Specific Methods

    list.append(value) #appends a value to the end of the list.
    list.pop(index) #remove a value at given position. if no parameter is passed, it will remove the last value in the list.
    list.index(value) #returns the index (position) of the given value if it exists in the list and raises an error if it does not exist.
    list.reverse() #reverses the order of the elements, in place.*
    list.sort() #sorts the items in order of least to greatest, or alphabetically for strings, in place.*
# * "In place" means it changes that same array, instead of returning a new array.
# https://docs.python.org/3/tutorial/datastructures.html
