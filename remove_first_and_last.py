""" 
Codewars Kata Training
Python Fundamentals

It's pretty straightforward. Your goal is to create a function that removes the first and last characters of a string. 
You're given one parameter, the original string. 

You don't have to worry with strings with less than two characters.

"""

def remove_char(s):
    
    # I used a slice that starts at the 's[1]' index and had a '-1' step, so that the last character isnt output.
    return s[1:-1]

