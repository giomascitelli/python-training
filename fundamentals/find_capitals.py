""" 
Codewars Kata Training
Python Fundamentals

Write a function that takes a single string (word) as argument. 
The function must return an ordered list containing the indexes of all capital letters in the string.

Example
Test.assertSimilar( capitals('CodEWaRs'), [0,3,4,6] );

"""

def capitals(word):
    index = []
    
    for i, char in enumerate(word):
        
        if char.isupper():
            index.append(i)
        
    return index

