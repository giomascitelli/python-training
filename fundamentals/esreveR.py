""" 
Codewars Kata Training
Python Fundamentals

Write a function reverse which reverses a list (or in clojure's case, any list-like data structure)

(the dedicated builtin(s) functionalities are deactivated)

You are not allowed to use the following:
    - python 2
    - slice notations
    - defining an empty list: []. Use " x = list() " instead
    - list comprehensions
    - the spread operator inside square brackets
    - "tuple" and "reversed" builtins have been deactivated

The "list" builtin has been replaced with another implementation with the following specifications:
    - list.reverse is forbidden
    - list.__reversed__ is forbidden
    - slicing is forbidden
All other usual methods of the list class are still present.

def reverse(lst):    
    empty_list = list()            # use this!

"""

def reverse(lst):
    empty_list = list()
    
    for i in lst:
        empty_list.insert(0, i)
    
    return empty_list

    