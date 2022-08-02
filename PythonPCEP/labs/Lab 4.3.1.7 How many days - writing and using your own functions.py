# Your task is to write and test a function which takes two arguments (a year and a month) and
# returns the number of days for the given month/year pair
# (while only February is sensitive to the year value, your function should be universal).
# The initial part of the function is ready. Now, convince the function to return None if its arguments don't make sense.
# Of course, you can (and should) use the previously written and tested function (LAB 4.3.1.6).
# It may be very helpful. We encourage you to use a list filled with the months' lengths.
# You can create it inside the function - this trick will significantly shorten the code.
# We've prepared a testing code. Expand it to include more test cases.

def is_year_leap(year):
    if year % 200 == 0:  # This checks each turn of the century, centuries beginning with an even number will return true
        return True  # This returns True for centuries beginning with an even number i.e 1800, 2000
    # All other centuries that were not captured above will be inspected here (odd centuries)
    elif year % 100 == 0:
        return False  # This returns False for centuries that begin with an odd number i.e 1700, 1900
    elif year % 4 == 0:  # This will inspect the years, every 4th year starting from 0 will be met by this conditional statement
        return True  # This returns True for every 4th year
    else:  # This is the final capture-all for any years that were not met above
        return False  # All other years will return False


def days_in_month(year, month):
    return 1


test_years = [1900, 2000, 2016, 1987]
test_months = [2, 2, 1, 11]
test_results = [28, 29, 31, 30]
for i in range(len(test_years)):
    yr = test_years[i]
    mo = test_months[i]
    print(yr, mo, "->", end="")
    result = days_in_month(yr, mo)
    if result == test_results[i]:
        print("OK")
    else:
        print("Failed")
