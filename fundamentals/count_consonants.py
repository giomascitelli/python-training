""" 
Codewars Kata Training
Python Fundamentals

Complete the function that takes a string of English-language text and returns the number of consonants in the string.

Consonants are all letters used to write English excluding the vowels a, e, i, o, u.

"""

import re

def consonant_count(s):
    return len(re.findall(r'[bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ]', s))

