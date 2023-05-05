""" 
Codewars Kata Training
Python Fundamentals

You get an array of numbers, return the sum of all of the positives ones.

Example [1,-4,7,12] => 1 + 7 + 12 = 20

Note: if there is nothing to sum, the sum is default to 0.

"""

def positive_sum(arr):
    
    # Using list comprehension and the sum function to get the sum of only positive numbers. The code only sums the results of the loop created where:
    # For each 'num' in 'arr', if the 'num' is a positive number, then they get summed.
    return sum(num for num in arr if num > 0)

