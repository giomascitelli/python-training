""" 
Codewars Kata Training
Python Fundamentals

Our football team has finished the championship.

Our team's match results are recorded in a collection of strings. Each match is represented by a string in the format "x:y", where x is our team's score and y is our opponents score.

For example: ["3:1", "2:2", "0:1", ...]

Points are awarded for each match as follows:

if x > y: 3 points (win)
if x < y: 0 points (loss)
if x = y: 1 point (tie)
We need to write a function that takes this collection and returns the number of points our team (x) got in the championship by the rules given above.

Notes:

our team always plays 10 matches in the championship
0 <= x <= 4
0 <= y <= 4

"""

def points(games):
    # First I did the win/draw/lose conditions and then converted each match in the games list to a tuple of integers using 'map' and used 'sum' to get the total.
	return sum(3 if x > y else 1 if x == y else 0 for x, y in (map(int, match.split(":")) for match in games))

