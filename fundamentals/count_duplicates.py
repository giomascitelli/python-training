""" 
Codewars Kata Training
Python Fundamentals

Write a function that will return the count of distinct case-insensitive alphabetic characters and numeric digits that occur more than once in the input string. 
The input string can be assumed to contain only alphabets (both uppercase and lowercase) and numeric digits.

"""

def duplicate_count(text):
    originals = set()
    duplicates = set()
    
    # As sets can't have repeated values in it, the for loop goes through the original text and if a 'char' is not already in the 'originals' set, then it is added
    # there. If it's already present in that set, its added to the 'duplicates', and then return the length of the 'duplicates' set.
    for char in text.lower():
            if char in originals:
                duplicates.add(char)
            else:
                originals.add(char)
                
    return len(duplicates)

     