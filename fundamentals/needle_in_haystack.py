""" 
Codewars Kata Training
Python Fundamentals

Write a function find_needle() that takes an array full of junk but containing one "needle"

After your function finds the needle it should return a message (as a string) that says:

"found the needle at position " plus the index it found the needle, so:

Example(Input --> Output)

["hay", "junk", "hay", "hay", "moreJunk", "needle", "randomJunk"] --> "found the needle at position 5"

"""

def find_needle(haystack):
    
    # In this code, I use the string method "index()" and concatenate it to the requested text so that we get the position of the string 'needle' on the array.
    return "found the needle at position " + str(haystack.index("needle"))

