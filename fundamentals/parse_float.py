""" 
Codewars Kata Training
Python Fundamentals

Write function parse_float which takes a string/list and returns a number or 'none' if conversion is not possible.

"""

def parse_float(string):
    return float(string) if isinstance(string, str) and string.replace('.', '', 1).isdigit() else None
    
    