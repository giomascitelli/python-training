""" 
Codewars Kata Training
Python Fundamentals

Take an array and remove every second element from the array. Always keep the first element and start removing with the next element.

Example:
["Keep", "Remove", "Keep", "Remove", "Keep", ...] --> ["Keep", "Keep", "Keep", ...]

"""

def remove_every_other(my_list):
    # I used list slicing to return every other string in the list.
    return my_list[::2]

