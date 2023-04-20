""" 
Codewars Kata Training
Python Fundamentals

Complete the function that accepts a string parameter, and reverses each word in the string. All spaces in the string should be retained.

Examples:

"This is an example!" ==> "sihT si na !elpmaxe"
"double  spaces"      ==> "elbuod  secaps"

"""

def reverse_words(text):
    
    # I used List Comprehension to iterate over the list 'reversed_words' and use slices '[::-1]' to make every word in the list backwards without changing
    # their positions, and then 'split(' ')' with a space as the argument, which splits the string on spaces only.
    reversed_words = (word[::-1] for word in text.split(' '))
    
    # The join() method is used to concatenate the reversed words back into a single string, using a space as the separator between the words.
    reversed_text = ' '.join(reversed_words)
    return reversed_text

