""" 
Codewars Kata Training
Python Fundamentals

Write a function that returns a string in which firstname is swapped with last name.

Example(Input --> Output)

"john McClane" --> "McClane john"

"""

def name_shuffler(str_):
    first_name, last_name = str_.split()
    
    return last_name + ' ' + first_name

