# Task 2: Leap Year Logic

def is_leap_year(year):
    """Return True if year is a leap year, otherwise False."""
    return (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0)


year = int(input("Enter a year: "))

if is_leap_year(year):
    print(year, "is a leap year.")
else:
    print(year, "is not a leap year.")
