""" 
Codewars Kata Training
Python Fundamentals

Create a class Ball. Ball objects should accept one argument for "ball type" when instantiated.

If no arguments are given, ball objects should instantiate with a "ball type" of "regular."

ball1 = Ball()
ball2 = Ball("super")
ball1.ball_type  #=> "regular"
ball2.ball_type  #=> "super"

"""

class Ball(object):
    
    # The initializer method accepts one argument 'ball_type', which has a default value of 'regular'
    def __init__(self, ball_type='regular'):
        
        # Then, the code assigns the value of the ball_type argument to the ball_type attribute of the object
        self.ball_type = ball_type
        
        