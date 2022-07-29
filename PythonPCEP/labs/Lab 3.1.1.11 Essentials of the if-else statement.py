#Personal Income Tax (PIT for short) had to be paid once a year, and was evaluated using the following rule:
#If income was not higher than 85,528 thalers, the tax was equal to 18% of the income minus 556 thalers and 2 cents
#If income was higher than this amount, the tax was equal to 14,839 thalers and 2 cents, plus 32% of the surplus over 85,528 thalers.
#Your task is to write a tax calculator.
#It should accept one floating-point value: the income.
#Next, it should print the calculated tax, rounded to full thalers. There's a function named round() which will do the rounding for you
#If the calculated tax is less than zero, it only means no tax at all (the tax is equal to zero). Take this into consideration during your calculations.

#This Lab was created by Luke G on 27 Jul 22 at 1745
print("Lab 3.1.1.11 Essentials of the if-else statement")
income = float(input("Enter the annual income: "))  #This takes the variable and prompts the user to assign a floating point to it

if income <= 85528: #The first comparison operator will conditionally execute if the variable named input is less than or equal to 85528
    tax = (income * 0.18) - 556.02 #This creates the variable named tax and assigns a value to it - calculates the tax, parenthesis are not required but have been inserted for clarity
    if tax < 0: #This nested comparison operator will execute only if the calculated tax from line 13 is less than 0
        tax = 0.0 #This takes the variable named tax and hard codes a floating point of 0.0
        
else: #If the first comparison operator on line 12 is not met, this else statement will be executed
    tax = 14839.02 + ((income - 85528)*0.32)  #This creates the variable named tax and assigns a value to it

tax = round(tax, 0) #This takes the variable named tax and assigns the same value rounded to a whole floating point
print("The tax is:", tax, "thalers") #This prints the calculated tax
