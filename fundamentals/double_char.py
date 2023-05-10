""" 
Codewars Kata Training
Python Fundamentals

Given a string, you have to return a string in which each character (case-sensitive) is repeated once.

Examples (Input -> Output):

  "String"      -> "SSttrriinngg"
  "Hello World" -> "HHeelllloo  WWoorrlldd"
  "1234!_ "     -> "11223344!!__  "

"""

def double_char(s):
    # I use list comprehension to iterate over each character and repeat it and then 'join' to output a single string.
    return "".join([char * 2 for char in s])

