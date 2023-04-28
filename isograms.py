""" 
Codewars Kata Training
Python Fundamentals

An isogram is a word that has no repeating letters, consecutive or non-consecutive. Implement a function that determines whether a string that contains only letters is an isogram. Assume the empty string is an isogram. Ignore letter case.

Example: (Input --> Output)

"Dermatoglyphics" --> true "aba" --> false "moOse" --> false (ignore letter case)

isIsogram "Dermatoglyphics" = true
isIsogram "moose" = false
isIsogram "aba" = false

"""

def is_isogram(string):
    
    # The code gets the length of the original input in 'len(string)' and compares it to the length of the same input(ignoring letter case), but turned into a set.
    # A set is a kind of list in Python that doesn't allow duplicates, so if 'len(string)' is equal to this set, then the code outputs 'True'.
    # Which means no letter was repeated.
    return len(string) == len(set(string.lower()))

