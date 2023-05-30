""" 
Codewars Kata Training
Python Fundamentals

Implement String#digit? (in Java StringUtils.isDigit(String)), which should return true if given object is a digit (0-9), false otherwise.

"""

def is_digit(n):
    return len(n) == 1 and n.isdigit()

