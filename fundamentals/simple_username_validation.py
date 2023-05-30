""" 
Codewars Kata Training
Python Fundamentals

Write a simple regex to validate a username. Allowed characters are:

lowercase letters,
numbers,
underscore

Length should be between 4 and 16 characters (both included).

"""

import re

def validate_usr(username):
    return bool(re.match(r'^(?=.{4,16}$)[a-z0-9_]+$', username))

