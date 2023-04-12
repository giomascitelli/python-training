""" 
Codewars Kata Training
Python Fundamentals

Build a function that returns an array of integers from n to 1 where n>0.

Example : n=5 --> [5,4,3,2,1]

"""

def reverse_seq(n):
    result = []
    
    # Create a 'for' loop and use the 'range()' function where 'n' is the start, '0' is the stop (as n > 0) and '-1' as the
    # step, since we want the array to go backwards.
    
    for i in range(n, 0, -1):
        result.append(i)
    print(result)

reverse_seq(int(input()))

