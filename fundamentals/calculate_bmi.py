""" 
Codewars Kata Training
Python Fundamentals

Write function bmi that calculates body mass index (bmi = weight / height2).

if bmi <= 18.5 return "Underweight"

if bmi <= 25.0 return "Normal"

if bmi <= 30.0 return "Overweight"

if bmi > 30 return "Obese"

"""

def bmi(weight, height):
    bmi_calc = (weight / height ** 2) 
    
    if bmi_calc <= 18.5:
        return "Underweight"
    elif bmi_calc <= 25.0:
        return "Normal"
    elif bmi_calc <= 30.0:
        return "Overweight"
    return "Obese"

