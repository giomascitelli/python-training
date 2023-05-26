""" 
Codewars Kata Training
Python Fundamentals

When provided with a number between 0-9, return it in words.

Input :: 1

Output :: "One".

If your language supports it, try using a switch statement.

"""

def switch_it_up(number):
    
    # Since Python doesn't have a built-in switch statement, the closest I could get to it was using a dictionary.
    word_dict = {
        0: "Zero",
        1: "One",
        2: "Two",
        3: "Three",
        4: "Four",
        5: "Five",
        6: "Six",
        7: "Seven",
        8: "Eight",
        9: "Nine"
    }
    
    return word_dict.get(number)

