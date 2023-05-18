""" 
Codewars Kata Training
Python Fundamentals

Given an integral number, determine if it's a square number:

In mathematics, a square number or perfect square is an integer that is the square of an integer; in other words, it is the product of some integer with itself.

The tests will always use some integral number, so don't worry about that in dynamic typed languages.

Examples
-1  =>  false
 0  =>  true
 3  =>  false
 4  =>  true
25  =>  true
26  =>  false

"""

def is_square(n):
    
    # First calculate 'n ** 0.5' to calculate the square root, and then check if the square root of n powered by 2 is equal to 'n'.    
    return (n ** 0.5) ** 2 == n

