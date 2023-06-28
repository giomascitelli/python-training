""" 
Codewars Kata Training
Python Fundamentals

Given an integer n and two other values, build an array of size n filled with these two values alternating.

Examples

5, true, false     -->  [true, false, true, false, true]
10, "blue", "red"  -->  ["blue", "red", "blue", "red", "blue", "red", "blue", "red", "blue", "red"]
0, "one", "two"    -->  []

"""

def alternate(n, first_value, second_value):
    return [first_value if i % 2 == 0 else second_value for i in range(n)]

