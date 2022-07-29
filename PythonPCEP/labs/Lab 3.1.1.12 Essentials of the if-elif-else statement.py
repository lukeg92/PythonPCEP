#Since the introduction of the Gregorian calendar (in 1582), the following rule is used to determine the kind of year:
#if the year number isn't divisible by four, it's a common year;
#otherwise, if the year number isn't divisible by 100, it's a leap year;
#otherwise, if the year number isn't divisible by 400, it's a common year;
#otherwise, it's a leap year.
#The code should output one of two possible messages, which are Leap year or Common year, depending on the value entered.
#It would be good to verify if the entered year falls into the Gregorian era, and output a warning otherwise: 
#Not within the Gregorian calendar period. 
#Tip: use the != and % operators.

#This lab was created by Luke G on 28 Jul 22 at 1130
print("Lab 3.1.1.12 Essentials of the if-elif-else statement")
year = int(input("Enter a year: ")) #This prompts the user to input an integer which will be assignes to the variable named year

if year < 1582: #This conditional statement will check if year is less than 1582. If the statement is True, the code will execute line 16 only. If False, it moves to line 18
    print("Not within the Gregorian calendar period")
    
elif year % 4 != 0: #This conditional statement will check if year is divisible by ecxactly 4. If the statement is True, the code will execute line 19 only. If False, it moves to line 21
    print("Common year")
    
elif year % 100 != 0: #This conditional statement will check if year is divisible by ecxactly 100. If the statement is True, the code will execute line 22 only. If False, it moves to line 24
    print("Leap year")
    
elif year % 400 != 0: #This conditional statement will check if year is divisible by ecxactly 400. If the statement is True, the code will execute line 25 only. If False, it moves to line 27
    print("Common year")
    
else: #If none of the above conditional statements have been met, the code will execute line 28
    print("Leap year")
