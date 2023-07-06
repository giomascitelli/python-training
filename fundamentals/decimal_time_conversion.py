""" 
Codewars Kata Training
Python Fundamentals

Write two functions, one that converts standard time to decimal time and one that converts decimal time to standard time.

One hour has 100 minutes (or 10,000 seconds) in decimal time, yet its duration is the same as in standard time. Thus a decimal minute consists of 36 standard seconds, which is 1/100 of an hour.
Working time is usually rounded to integer decimal minutes. Thus one standard minute equals 0.02 decimal hours, while two standard minutes equal 0.03 decimal hours and so on.
to_industrial(time) should accept either the time in minutes as an integer or a string of the format "h:mm". Minutes will always consist of two digits in the tests (e.g., "0:05"); hours can have more. Return a float that represents decimal hours (e.g. 1.75 for 1h 45m). Round to a precision of two decimal digits - do not simply truncate!
to_normal(time) should accept a float representing decimal time in hours. Return a string that represents standard time in the format "h:mm".
There will be no seconds in the tests. We'll neglect them for the purpose of this kata.

Examples:
to_industrial(1) => 0.02
to_industrial("1:45") => 1.75
to_normal(0.33) => "0:20"

"""

def to_industrial(time):
    if isinstance(time, str):
        hours, minutes = map(int, time.split(':'))
        decimal_hours = hours + (minutes / 60)
        return round(decimal_hours, 2)
    else:
        return round(time / 60, 2)


def to_normal(time):
    hours = int(time)
    minutes = round((time - hours) * 60)
    return f"{hours}:{minutes:02d}"

