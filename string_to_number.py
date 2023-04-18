""" 
Codewars Kata Training
Python Fundamentals

We need a function that can transform a string into a number. What ways of achieving this do you know?

Note: Don't worry, all inputs will be strings, and every string is a perfectly valid representation of an integral number.

Examples:

"1234" --> 1234
"605"  --> 605
"1405" --> 1405
"-7" --> -7

"""

def string_to_number(s):
    
    # I use the 'int()' built-in method to transform anything into a 'int'.
    return int(s)

