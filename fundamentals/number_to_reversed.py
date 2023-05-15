""" 
Codewars Kata Training
Python Fundamentals

Given a random non-negative number, you have to return the digits of this number within an array in reverse order.

Example(Input => Output):
35231 => [1,3,2,5,3]
0 => [0]

"""

def digitize(n):
    
    # Using map to apply the 'int' function to every digit while converting the 'n' into a string and slice it so that it's reversed.
    return map(int, str(n)[::-1])

