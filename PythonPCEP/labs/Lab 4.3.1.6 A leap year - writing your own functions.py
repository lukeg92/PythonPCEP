# Your task is to write and test a function which takes one argument (a year) and returns True if the year is a leap year, or False otherwise.
# The seed of the function is already sown in the skeleton code in the editor.
# Note: we've also prepared a short testing code, which you can use to test your function.
# The code uses two lists - one with the test data, and the other containing the expected results.
# The code will tell you if any of your results are invalid.

# This lab was created by Luke G on 2 Aug 22 at 1910
print("\nLab 4.3.1.6 A leap year - writing your own functions\n")


def is_year_leap(year):  # The function to be defined is called is_leap_year. (year) will be the argument that is inspected in the programme
    if year % 200 == 0:  # This checks each turn of the century, centuries beginning with an even number will return true
        return True  # This returns True for centuries beginning with an even number i.e 1800, 2000
    # All other centuries that were not captured above will be inspected here (odd centuries)
    elif year % 100 == 0:
        return False  # This returns False for centuries that begin with an odd number i.e 1700, 1900
    elif year % 4 == 0:  # This will inspect the years, every 4th year starting from 0 will be met by this conditional statement
        return True  # This returns True for every 4th year
    else:  # This is the final capture-all for any years that were not met above
        return False  # All other years will return False


test_data = [1900, 2000, 2016, 1987]
test_results = [False, True, True, False]
for i in range(len(test_data)):
    yr = test_data[i]
    print(yr, "->", end="")
    result = is_year_leap(yr)
    if result == test_results[i]:
        print("OK")
    else:
        print("Failed")
