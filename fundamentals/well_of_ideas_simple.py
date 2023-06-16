""" 
Codewars Kata Training
Python Fundamentals

For every good kata idea there seem to be quite a few bad ones!

In this kata you need to check the provided array (x) for good ideas 'good' and bad ideas 'bad'. If there are one or two good ideas, return 'Publish!', if there are more than 2 return 'I smell a series!'. If there are no good ideas, as is often the case, return 'Fail!'.

"""

def well(x):
    count = sum(1 for i in x if i == 'good')

    return 'Fail!' if count == 0 else 'Publish!' if count <= 2 else 'I smell a series!'

