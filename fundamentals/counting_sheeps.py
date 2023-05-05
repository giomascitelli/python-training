""" 
Codewars Kata Training
Python Fundamentals

The first century spans from the year 1 up to and including the year 100, the second century - from the year 101 up to and including the year 200, etc.

Task
Given a year, return the century it is in.

Examples
1705 --> 18
1900 --> 19
1601 --> 17
2000 --> 20

"""

def count_sheep(n):
    # Initiate an empty string to receive the loop results
    sheep_count = ""
    
    # Loop between '1' and 'n+1' because the upper bound of the 'range()' function is not inclusive. This means that the second value will never be output.
    # So if the user inputs '2', the range would be 'range(1, 3)', since '3' is the upper bound, the ouput would be '1 and 2'.
    for i in range(1, n+1):
        sheep_count += f"{i} sheep..."
    return sheep_count

