""" 
Codewars Kata Training
Python Fundamentals

Write a function that will accept two parameters: variable and type and check if type of variable is matching type. Return true if types match or false if not.

Examples:
42, "int"    --> True
"42", "int"  --> False

"""

def type_validation(variable, _type): 
    return type(variable).__name__ == _type

