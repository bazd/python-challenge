"""Script to accept a number and tell you if it's a leap year
   Author Barry Dawson 
   Python 3
"""

def leap_year_check(year):
    # Function to return True if leap year, and False if not    
    
    century_check = year / 100
    if int(century_check):
        print(year, 'is a century year')
        leap_century_check = year / 400
        if int(leap_century_check):
            print(year, 'is a leap year')
            return True
        else:
            print(year, 'is not a leap year')
            return False
    
    leap_check = year / 4
    if int(leap_check):
        print(year, 'is a leap year')
        return True
    else:
        print(year, 'is not a leap year')
        return False     


year = input("Enter a year to check if it's a leap year: ")
year = int(year) # Convert string input to integer
result = leap_year_check(year)
print(result)