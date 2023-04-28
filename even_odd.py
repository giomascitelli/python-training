""" 
Codewars Kata Training
Python Fundamentals

Create a function that takes an integer as an argument and returns "Even" for even numbers or "Odd" for odd numbers.

"""


def even_or_odd(number):
    
    # Using a ternary conditional operator we can write this condition in a single line of code where if the division of 'number' and '2' has a modulus equal to '0'
    # the 'number' is "Even". If the 'number' doesn't meet these conditions, then it's "Odd".
    return "Even" if number % 2 == 0 else "Odd"

