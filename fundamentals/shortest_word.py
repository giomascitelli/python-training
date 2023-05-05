""" 
Codewars Kata Training
Python Fundamentals

Simple, given a string of words, return the length of the shortest word(s).

String will never be empty and you do not need to account for different data types.

"""

def find_short(s):
    words = s.split()
    
    # Make a variable that holds the length of the first word of the given string.
    shortest_word = len(words[0])
    
    # Loop over the words in the string, where if one of the words is smaller than the first word of the string, the variable will be updated with the smallest.
    for word in words:
        if len(word) < shortest_word:
            shortest_word = len(word)
            
    return shortest_word

