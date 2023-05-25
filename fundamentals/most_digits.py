""" 
Codewars Kata Training
Python Fundamentals

Find the number with the most digits.

If two numbers in the argument array have the same number of digits, return the first one in the array.

"""

def find_longest(arr):
    
    return max(arr, key=lambda x: len(str(x)))

