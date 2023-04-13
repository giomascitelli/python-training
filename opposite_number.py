""" 
Codewars Kata Training
Python Fundamentals

Given an integer or a floating-point number, find its opposite.

Examples:

1: -1
14: -14
-34: 34

"""

def opposite(number):
    
    """ Assuming 'number' is '1': 
    Since '1 + 1' is the same as '1 * 2', then we have the following calculation step by step:
        1 - (1 + 1) =
        1 - 2 =
        -1 
    """
    return number - (number*2)

