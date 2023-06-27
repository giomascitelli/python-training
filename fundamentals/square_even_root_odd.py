""" 
Codewars Kata Training
Python Fundamentals

Complete the function that takes a list of numbers (nums), as the only argument to the function. 
Take each number in the list and square it if it is even, or square root the number if it is odd. 
Take this new list and return the sum of it, rounded to two decimal places.

The list will never be empty and will only contain values that are greater than or equal to zero.

"""

from math import sqrt

def sum_square_even_root_odd(nums):
    return round(sum([i ** 2 if i % 2 == 0 else sqrt(i) for i in nums]), 2)

