""" 
Codewars Kata Training
Python Fundamentals

Your task is to write function factorial.

"""

def factorial(n):
    result = 1
    
    for i in range(1, n+1):
        result *= i
    
    return result

