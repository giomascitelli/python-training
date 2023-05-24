""" 
Codewars Kata Training
Python Fundamentals

Description:
Remove n exclamation marks in the sentence from left to right. n is positive integer.

Examples

remove("Hi!",1) === "Hi"
remove("Hi!",100) === "Hi"
remove("Hi!!!",1) === "Hi!!"

"""

def remove(s, n):
    return s.replace('!', '', n)

