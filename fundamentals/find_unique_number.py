""" 
Codewars Kata Training
Python Fundamentals

There is an array with some numbers. All numbers are equal except for one. Try to find it!

find_uniq([ 1, 1, 1, 2, 1, 1 ]) == 2
find_uniq([ 0, 0, 0.55, 0, 0 ]) == 0.55
It’s guaranteed that array contains at least 3 numbers.

The tests contain some very huge arrays, so think about performance.

"""

def find_uniq(arr):
    
    # Sets can only carry unique values
    a, b = set(arr)
    
    # So from the two remaining values, we compare them to the original input array and use 'count()' to check which one is unique and output it.
    return a if arr.count(a) == 1 else b

