""" 
Codewars Kata Training
Python Fundamentals

Description:
Replace all vowel to exclamation mark in the sentence. aeiouAEIOU is vowel.

Examples

replace("Hi!") === "H!!"
replace("!Hi! Hi!") === "!H!! H!!"

"""

def replace_exclamation(s):
    vowels = 'aeiouAEIOU'
    return ''.join(['!' if char in vowels else char for char in s])

