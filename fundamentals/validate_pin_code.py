""" 
Codewars Kata Training
Python Fundamentals

ATM machines allow 4 or 6 digit PIN codes and PIN codes cannot contain anything but exactly 4 digits or exactly 6 digits.

If the function is passed a valid PIN string, return true, else return false.

Examples (Input --> Output)
"1234"   -->  true
"12345"  -->  false
"a234"   -->  false

"""

def validate_pin(pin):
    
    # The function checks if the length of the input pin is either 4 or 6, and if that's True, then it checks if all of the values are numbers with 'isdigit()'.
    return len(pin) in [4, 6] and pin.isdigit()

