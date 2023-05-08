""" 
Codewars Kata Training
Python Fundamentals

You will be given a number and you will need to return it as a string in Expanded Form. For example:

expanded_form(12) # Should return '10 + 2'
expanded_form(42) # Should return '40 + 2'
expanded_form(70304) # Should return '70000 + 300 + 4'

NOTE: All numbers will be whole numbers greater than 0.

"""

def expanded_form(num):

    quotient = num
    place_value = 1
    expanded = []

    # The loop goes through the numbers from right to left dividing the 'quotient' by 10 and keeping track of the remainder. If the digit is not zero, then the
    # code calculates the value multiplying it by 'place_value' and store the result as a string on the 'expanded' list.
    
    while quotient > 0:
        digit = quotient % 10
        
        if digit != 0:
            value = digit * place_value
        
            expanded.append(str(value))
        
        quotient //= 10
        
        place_value *= 10

    # The list is reversed using slicing since the loop was from right to left and 'join' the values with '+'.
    return " + ".join(expanded[::-1])

