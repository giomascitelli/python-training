""" 
Codewars Kata Training
Python Fundamentals

The main idea is to count all the occurring characters in a string. If you have a string like aba, then the result should be {'a': 2, 'b': 1}.

What if the string is empty? Then the result should be empty object literal, {}.

"""

def count(s):
    
    result = {}
    
    # Loop goes through every 'char' in 's' and checks if the 'char' is already in the 'result' dictionary created earlier. If it isn't, the char is added with
    # value of 1. If it's already in the dictionary, then it adds 1 to the respective char value.
    for char in s:
        if char in result:
            result[char] += 1
        else:
            result[char] = 1
    return result
                
    