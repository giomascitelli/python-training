""" 
Codewars Kata Training
Python Fundamentals

Given an array of integers.

Return an array, where the first element is the count of positives numbers and the second element is sum of negative numbers. 0 is neither positive nor negative.

If the input is an empty array or is null, return an empty array.

Example:

For input [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15], you should return [10, -65].

"""

def count_positives_sum_negatives(arr):
    
    if len(arr) == 0:
        return []
    
    count_positives = 0
    sum_negatives = 0
    
    # The following loop iterates over the given 'arr' and uses a counter to update the 'count_positives' and 'sum_negatives' values if the conditions are met.
    for num in arr:
        if num < 0:
            count_positives += 1
        else:
            sum_negatives += num
    
    return [count_positives, sum_negatives]

