""" 
Codewars Kata Training
Python Fundamentals

Create a function which translates a given DNA string into RNA.

For example:

"GCAT"  =>  "GCAU"

The input string can be of arbitrary length - in particular, it may be empty. All input is guaranteed to be valid, i.e. each input string will only ever consist of 'G', 'C', 'A' and/or 'T'.

"""

def dna_to_rna(dna):
    # The replace method replaces the first argument "T" with the second "U".
    return dna.replace("T", "U")

    