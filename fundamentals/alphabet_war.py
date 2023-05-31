""" 
Codewars Kata Training
Python Fundamentals

Write a function that accepts fight string consists of only small letters and return who wins the fight. When the left side wins return Left side wins!, when the right side wins return Right side wins!, in other case return Let's fight again!.

The left side letters and their power:

 w - 4
 p - 3
 b - 2
 s - 1
 
The right side letters and their power:

 m - 4
 q - 3
 d - 2
 z - 1
 
The other letters don't have power and are only victims.

Example

AlphabetWar("z");        //=> Right side wins!
AlphabetWar("zdqmwpbs"); //=> Let's fight again!
AlphabetWar("zzzzs");    //=> Right side wins!
AlphabetWar("wwwwwwz");  //=> Left side wins!

"""

def alphabet_war(fight):
    left_values = sum(4 if letter == 'w' else 3 if letter == 'p' else 2 if letter == 'b' else 1 if letter == 's' else 0 for letter in fight)
    
    right_values = sum(4 if letter == 'm' else 3 if letter == 'q' else 2 if letter == 'd' else 1 if letter == 'z' else 0 for letter in fight)
    
    return "Left side wins!" if left_values > right_values else "Right side wins!" if right_values > left_values else "Let's fight again!"
    
    