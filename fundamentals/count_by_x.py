""" 
Codewars Kata Training
Python Fundamentals

Create a function with two arguments that will return an array of the first n multiples of x.

Assume both the given number and the number of times to count will be positive numbers greater than 0.

Return the results as an array or list ( depending on language ).

Examples:

count_by(1,10) #should return [1,2,3,4,5,6,7,8,9,10]
count_by(2,5) #should return [2,4,6,8,10]

"""

def count_by(x, n):
    
    # The range creates a 'x' start, a '(n+1)*x' stop and an 'x' step.
    return list(range(x,(n+1)*x, x))  # '(n+1) since the stop is not included and '*x' because the prompt says 'the first n multiples of x'.

