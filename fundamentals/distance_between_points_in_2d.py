""" 
Codewars Kata Training
Python Fundamentals

Point objects have attributes x and y.

Write a function calculating distance between Point a and Point b.

Tests compare expected result and actual answer with tolerance of 1e-6.

"""

import math

def distance_between_points(a, b):
    
    return math.sqrt((b.y - a.y) ** 2 + (b.x - a.x) ** 2)

