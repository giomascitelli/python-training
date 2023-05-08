""" 
Codewars Kata Training
Python Fundamentals

Implement the function unique_in_order which takes as argument a sequence 
and returns a list of items without any elements with the same value next to each other and preserving the original order of elements.

For example:

unique_in_order('AAAABBBCCDAABBB') == ['A', 'B', 'C', 'D', 'A', 'B']
unique_in_order('ABBCcAD')         == ['A', 'B', 'C', 'c', 'A', 'D']
unique_in_order([1, 2, 2, 3, 3])   == [1, 2, 3]
unique_in_order((1, 2, 2, 3, 3))   == [1, 2, 3]

"""

def unique_in_order(sequence):
    unique_list = []
    last_element = None
    
    for i in sequence:
        if i is not last_element:
            unique_list.append(i)
            last_element = i
            
    return unique_list

