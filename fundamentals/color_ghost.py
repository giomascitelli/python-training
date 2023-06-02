""" 
Codewars Kata Training
Python Fundamentals

Create a class Ghost

Ghost objects are instantiated without any arguments.

Ghost objects are given a random color attribute of "white" or "yellow" or "purple" or "red" when instantiated

ghost = Ghost()
ghost.color  #=> "white" or "yellow" or "purple" or "red"

"""

import random

class Ghost(object):
    def __init__(self):
        self.colors = ["white", "yellow", "purple", "red"]
        
        self.color = random.choice(self.colors)
        
        