# Yvone Nicole B. Perlas | ID: 2023-904
# exercise 5: days of the month

days_in_month = {
    1: 31,  # January
    2: 28,  # February (assuming a non-leap year)
    3: 31,  # March
    4: 30,  # April
    5: 31,  # May
    6: 30,  # June
    7: 31,  # July
    8: 31,  # August
    9: 30,  # September
    10: 31,  # October
    11: 30,  # November
    12: 31,  # December
}

# After making a dictionary we need a place to store the values that
# will be input by the user.
month_number = int(input("Enter the month of your choice (1-12): "))

# This asks the user to enter a month number between 1-12 and then stores the value in the month_number variable.
if 1 <= month_number <= 12:  # Checks if the inputted number is within range of 1-12.
    print(f"There are {days_in_month[month_number]} days in month {month_number}.")
else:
    print("Invalid month number. Please enter a number between 1 and 12.")
    # Asks the user for a valid number within the range (1-12).

def is_leap_year(year):
    # This function checks if a given year is a leap year.
    if year % 4 == 0:  # This calculates if the year is divisible by 4.
        if year % 100 == 0:
            if year % 400 == 0:
                return True  # Divisible by 400, it is a leap year.
            else:
                return False  # Divisible by 100 but not by 400, not a leap year.
        else:
            return True  # Divisible by 4 but not by 100, it is a leap year.
    else:
        return False  # Not divisible by 4, not a leap year.

# You can test the is_leap_year function by calling it with a year.
year = int(input("Enter a year: "))
if is_leap_year(year):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")


