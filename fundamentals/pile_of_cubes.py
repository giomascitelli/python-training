""" 
Codewars Kata Training
Python Fundamentals

Your task is to construct a building which will be a pile of n cubes. 
The cube at the bottom will have a volume of n ** 3, the cube above will have volume of (n - 1) ** 3 and so on until the top which will have a volume of 1 ** 3.

You are given the total volume 'm' of the building. being given 'm' can you find the number of cubes you will have to build?

The parameter of the function 'find_nb' will be an integer 'm' and you have to return the integer 'n' such as:

n ** 3 + (n - 1) ** 3 + (n - 2) ** 3 + ... + 1 ** 3 = m 
if such a 'n' exists or -1 if there is no such 'n'.

Examples:
(Input) --> (Output)

find_nb(1071225) --> 45
find_nb(91716553919377) --> -1

"""

def find_nb(m):
    n = 1
    
    # A loop to keep subtracting the volume of the cubes starting from the largest cube until it reaches either exactly zero volume left or below zero.
    while m > 0:
        m -= n**3
        n += 1
    
    # If exactly zero, then return the current value of 'n' as the answer, else, return -1.    
    if m == 0:
        return n-1
    
    else:
        return -1

    