""" 
Codewars Kata Training
Python Fundamentals

You will be given an array and a limit value. 
You must check that all values in the array are below or equal to the limit value. 
If they are, return true. Else, return false.

You can assume all values in the array are numbers.

"""

def small_enough(array, limit):
    
    # The all function checks if every condition inside the list comprehension is True.
    return all(num <= limit for num in array)

