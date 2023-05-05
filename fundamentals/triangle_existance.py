""" 
Codewars Kata Training
Python Fundamentals

Implement a function that accepts 3 integer values a, b, c. 
The function should return true if a triangle can be built with the sides of given length and false in any other case.

(In this case, all triangles must have surface greater than 0 to be accepted).

"""

def is_triangle(a, b, c):
    # I use the triangles conditions of existance rules and if they are met, the ouput is 'True'.
    return True if (a+b) > c and (a+c) > b and (b+a) > c  and (b+c) > a else False


