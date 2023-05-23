""" 
Codewars Kata Training
Python Fundamentals

Input: Array of elements

["h","o","l","a"]

Output: String with comma delimited elements of the array in th same order.

"h,o,l,a"

"""

def print_array(arr):
    str_arr = map(str, arr)
    
    return ",".join(str_arr)

