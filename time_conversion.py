""" 
Codewars Kata Training
Python Fundamentals

Clock shows h hours, m minutes and s seconds after midnight.

Your task is to write a function which returns the time since midnight in milliseconds.

Example:
h = 0
m = 1
s = 1

result = 61000

Input constraints:

0 <= h <= 23
0 <= m <= 59
0 <= s <= 59

"""

def past(h, m, s):
    
    # If the input constraint isn't matched, the 'ValueError' will be raised.
    if not (0 <= h <= 23):
        raise ValueError("Wrong hour value.")
    if not (0 <= m <= 59):
        raise ValueError("Wrong minute value.")
    if not (0 <= s <= 59):
        raise ValueError("Wrong seconds value.")
        
    # Hours and minutes converted to seconds, and then to milliseconds.
    return (h*3600 + m*60 + s) * 1000

