""" 
Codewars Kata Training
Python Fundamentals

Given an array of numbers, check if any of the numbers are the character codes for lower case vowels (a, e, i, o, u).

If they are, change the array value to a string of that vowel.

Return the resulting array.

"""

def is_vow(inp):
    vowels = [97, 101, 105, 111, 117] 
    
    return [chr(num) if num in vowels else num for num in inp]

