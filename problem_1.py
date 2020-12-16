'''

Given a year, determine whether it is a leap year. If it is a leap year, return the Boolean True,
otherwise return False.
Note that the code stub provided reads from STDIN and passes arguments to the is_leap function. It is only necessary to

complete the is_leap function.
This means that in the Gregorian calendar, the years 2000 and 2400 are leap years, while 1800, 1900, 2100, 2200, 2300
and 2500 are NOT leap years.

# Input Format:
    Read , year the year to test

# Output Format:
    The function must return a Boolean value (True/False). Output is handled by the provided code stub.

'''

# Solve this problem :

def is_leap(year):
    if ((1900 <= year <= 3000 and year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)):
        leap = True
        return leap
    else:
        leap = False
        return leap

year = int(input())
print(is_leap(year))

