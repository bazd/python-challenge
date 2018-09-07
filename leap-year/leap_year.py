"""Script to accept a number and tell you if it's a leap year
   Author Barry Dawson 
   Python 3
"""

import argparse
parser = argparse.ArgumentParser()

def leap_year_check(year):
    # Function to return True if leap year, and False if not    

    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        print(year, 'is a leap year')
        return True
    else:
        print(year, 'is not a leap year')
        return False  

def main():
    year = input("Enter a year to check if it's a leap year: ")
    year = int(year) # Convert string input to integer
    result = leap_year_check(year)
    print(result)

if __name__ == "__main__":
    main()