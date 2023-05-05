""" 
Codewars Kata Training
Python Fundamentals

Given a string of digits, you should replace any digit below 5 with '0' and any digit 5 and above with '1'. Return the resulting string.

Note: input will never be an empty string

"""

def fake_bin(x):
    # The empty 'result' string receives the numbers from the 'for' loop that is iterating over 'x' input string.
    result = ""
    
    for num in x:
        if int(num) < 5:  # We have to use 'int()' so that the chars inside the string can be comparable to the number '5'.
            result += "0"
        else:
            result += "1"
    print(result)

fake_bin(input())
    
        