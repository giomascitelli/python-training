""" 
Codewars Kata Training
Python Fundamentals

Create a function that gives a personalized greeting. This function takes two parameters: name and owner.

Use conditionals to return the proper message:

name equals owner = 'Hello boss'
otherwise = 'Hello guest'

"""

def greet(name, owner):
    
    # Simple condition where if the name input is equal to the owner's name, then 'Hello boss' will be output. Otherwise, 'Hello guest' will be output.
    return "Hello boss" if name == owner else "Hello guest"

