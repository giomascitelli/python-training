""" 
Codewars Kata Training
Python Fundamentals

Given an integer (1 <= n <= 100) representing a person's age, return their minimum and maximum age range.

This equation doesn't work when the age <= 14, so use this equation instead:

min = age - 0.10 * age
max = age + 0.10 * age
You should floor all your answers so that an integer is given instead of a float (which doesn't represent age). Return your answer in the form [min]-[max]

##Examples:

age = 27   =>   20-40
age = 5    =>   4-5
age = 17   =>   15-20

"""

import math

def dating_range(age):
    if age <= 14:
        minimum = math.floor(age - 0.10 * age)
        maximum = math.floor(age + 0.10 * age)
    else:
        minimum = math.floor(age / 2 + 7)
        maximum = math.floor((age - 7) * 2)

    return f'{minimum}-{maximum}'

