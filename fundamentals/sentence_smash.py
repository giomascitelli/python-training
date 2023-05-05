""" 
Codewars Kata Training
Python Fundamentals

Sentence Smash
Write a function that takes an array of words and smashes them together into a sentence and returns the sentence. You can ignore any need to sanitize words or add punctuation, but you should add spaces between each word. Be careful, there shouldn't be a space at the beginning or the end of the sentence!

Example
['hello', 'world', 'this', 'is', 'great']  =>  'hello world this is great'

"""

def smash(words):
    # The join() function takes an empty separator ' ' and converts the elements in the array into one string.  
    sentence = ' '.join(words)
    return sentence

