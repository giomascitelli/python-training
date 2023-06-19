""" 
Codewars Kata Training
Python Fundamentals

Given the molecular mass of two molecules M1 and M2, their masses present m1 and m2 in a vessel of volume V at a specific temperature T, find the total pressure
P(total) exerted by the molecules. Formula to calculate the pressure is:

P(total) = (m1/M1 + m2/M2) * R * T / V

Input

Six values:

M1 and M2: molar masses of both gases, in grams (g)
m1 and m2: present mass of both gases, in g . mol^-1
V: volume of the vessel, in dm^3
T: temperature, in ºC

Output

One value: P(total), in units of atm.

Temperature is given in Celsius while SI unit is Kelvin (K). 0ºC = 273.15 K

The gas constant R = 0.082dm^3 . atm . K^-1 . mol^-1

"""

def solution(molar_mass1, molar_mass2, given_mass1, given_mass2, volume, temp) :
    kelvin_temp = temp + 273.15
    return (given_mass1/molar_mass1 + given_mass2/molar_mass2) * 0.082 * kelvin_temp / volume

