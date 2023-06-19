""" 
Codewars Kata Training
Python Fundamentals

This series of katas will introduce you to basics of doing geometry with computers.

Point objects have x, y attributes. Circle objects have center which is a Point, and radius, which is a number.

Write a function calculating circumference of a Circle.

Tests round answers to 6 decimal places.

"""

import math

def circle_circumference(circle):
    return round(2 * math.pi * circle.radius, 6)

