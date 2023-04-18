""" 
Codewars Kata Training
Python Fundamentals

Complete the solution so that it returns true if the first argument(string) passed in ends with the 2nd argument (also a string).

Examples:

solution('abc', 'bc') # returns True
solution('abc', 'd') # returns False

"""

def solution(text, ending):
    
    # The 'endswith()' method returns 'True' if the string ends with the specified value.
    return text.endswith(ending)

