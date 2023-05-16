""" 
Codewars Kata Training
Python Fundamentals

You are given the length and width of a 4-sided polygon. The polygon can either be a rectangle or a square.
If it is a square, return its area. If it is a rectangle, return its perimeter.

Example(Input1, Input2 --> Output):

6, 10 --> 32
3, 3 --> 9
Note: for the purposes of this kata you will assume that it is a square if its length and width are equal, otherwise it is a rectangle.

"""

def rps(p1, p2):
    # Simple ternary operation to do the conditions of the game
    return "Draw!" if p1 == p2 else f"Player {(1 if (p1=='rock' and p2=='scissors') or (p1=='paper' and p2=='rock') or (p1=='scissors' and p2=='paper') else 2)} won!"

