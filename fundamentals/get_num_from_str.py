""" 
Codewars Kata Training
Python Fundamentals

Write a function which removes from string all non-digit characters and parse the remaining to number. E.g: "hell5o wor6ld" -> 56

Function:

getNumberFromString(s)

"""

def get_number_from_string(string):
    digits = [int(char) for char in string if char.isdigit()]
    
    if digits:
        return (int("".join(map(str, digits))))
    
    else:
        return None
    
    