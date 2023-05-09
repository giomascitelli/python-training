""" 
Codewars Kata Training
Python Fundamentals

A pangram is a sentence that contains every single letter of the alphabet at least once. 
For example, the sentence "The quick brown fox jumps over the lazy dog" is a pangram, because it uses the letters A-Z at least once (case is irrelevant).

Given a string, detect whether or not it is a pangram. Return True if it is, False if not. Ignore numbers and punctuation.

"""

def is_pangram(s):
    
    # First I use 'lower()' to convert the input string since the case is irrelevant.
    s = s.lower()
    letters = "abcdefghijklmnopqrstuvwxyz"
    
    # Then, in this loop, if a character from the variable 'letters' is not present in 's', then the output is False.
    for char in letters:
        if char not in s:
            return False
            
    return True
        
