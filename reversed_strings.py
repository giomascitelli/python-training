""" 
Codewars Kata Training
Python Fundamentals

Complete the solution so that it reverses the string passed into it.

'world'  =>  'dlrow'
'word'   =>  'drow'

"""

def solution(string):
    # We use a slice in the 'string' and use the negative value of '-1' so that it slices backwards on the given string.
    return string[::-1]

