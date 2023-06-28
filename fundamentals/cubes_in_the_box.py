""" 
Codewars Kata Training
Python Fundamentals

Your job is to write a function f(x,y,z) to count how many cubes of any size can fit inside a x*y*z box. For example, a 2*2*3 box has 12 1*1*1 cubes, 2 2*2*2 cubes, so a total of 14 cubes in the end. See the animation below for a visual description of the task!

Notes:
x,y,z are strictly positive and will not be too big.

"""

def f(x, y, z):
    return sum((x-i)*(y-i)*(z-i) for i in range(min(x, y, z)))

