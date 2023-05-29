""" 
Codewars Kata Training
Python Fundamentals

Your task, is to create N×N multiplication table, of size provided in parameter.

For example, when given size is 3:

1 2 3
2 4 6
3 6 9
For the given example, the return value should be:

[[1,2,3],[2,4,6],[3,6,9]]

"""

def multiplication_table(size):
    
    # The code uses nested list comprehension where 'i' is in charge of creating the rows and 'j' creates the values within them. Each value is created by
    # multiplying the row number 'i' by the column number 'j'.
    return [[i * j for j in range(1, size+1)] for i in range (1, size+1)]

    