""" 
Codewars Kata Training
Python Fundamentals

Your task is to complete the Cat class which Extends Animal and replace the speak method to return the cats name + meows. e.g. 'Mr Whiskers meows.'
The name attribute is passed with this.name (JS), @name (Ruby) or self.name (Python).

"""

from preloaded import Animal

class Cat(Animal):
    def speak(self):
        return f'{self.name} meows.'
    
    