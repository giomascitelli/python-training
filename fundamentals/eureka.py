""" 
Codewars Kata Training
Python Fundamentals

The number 89 is the first integer with more than one digit that fulfills the property of: '89 = 8 ** 1 + 9 ** 2'

The next number in having this property is 135:

'135 = 1 ** 1 + 3 ** 2 + 5 ** 3'

We need a function to collect these numbers, that may receive two integers a, b that defines the range [a,b] (inclusive) 
and outputs a list of the sorted numbers in the range that fulfills the property described above.

Examples (Input -> Output):

1, 10 -> [1, 2, 3, 4, 5, 6, 7, 8, 9]
1, 100 -> [1, 2, 3, 4, 5, 6, 7, 8, 9, 89]

If there are no numbers of this kind in the range [a, b] the function should output an empty list.

"""

def sum_dig_pow(a, b):
    return [x for x in range(a, b+1) if sum(int(d)**i for i, d in enumerate(str(x), 1)) == x]

