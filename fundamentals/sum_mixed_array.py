""" 
Codewars Kata Training
Python Fundamentals

Given an array of integers as strings and numbers, return the sum of the array values as if all were numbers.

Return your answer as a number.

"""

def sum_mix(arr):
    # I used list comprehension to iterate over each element of the array and transform them into an 'int' so that every element and the ouput is a number.
    return sum([int(i) for i in arr])

