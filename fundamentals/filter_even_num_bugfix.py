""" 
Codewars Kata Training
Python Fundamentals

The method is supposed to remove even numbers from the list and return a list that contains the odd numbers.

However, there is a bug in the method that needs to be resolved.

def kata_13_december(lst): 
    # Fix this code
    for i in range(len(lst)): 
        if lst[i]%2==0: 
            lst.remove(i)
    return lst

"""

def kata_13_december(lst):
    odds_lst = []
    
    for i in lst:
        if i % 2 != 0: 
            odds_lst.append(i)
            
    return odds_lst

