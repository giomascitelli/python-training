""" 
Codewars Kata Training
Python Fundamentals

Consider an array/list of sheep where some sheep may be missing from their place. We need a function that counts the number of sheep present in the array (true means present).

For example:

[True,  True,  True,  False,
  True,  True,  True,  True ,
  True,  False, True,  False,
  True,  False, False, True ,
  True,  True,  True,  True ,
  False, False, True,  True]
  
The correct answer would be 17.

Hint: Don't forget to check for bad values like null/undefined

"""

def count_sheeps(sheep):
    sheep_count = 0
    
    # If the value inside 'sheep' is 'True', then we add '1' to the 'sheep_count' variable.
    for bool in sheep:
        if bool == True:
            sheep_count += 1
    return sheep_count

"""
Or in one line of code the solution could also be:

def count_sheeps(sheep):
    return sheep.count(True)
"""

