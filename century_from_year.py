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

def century(year):
    # We use the 'floor division' so that we get an integer as the result of 'year - 1' divided by '100'.
    return ((year - 1) // 100) + 1

