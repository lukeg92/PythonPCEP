#This Lab was completed by Luke G on 27 Jul 22 at 1700
#This Lab's objective is to:
#Write a program that utilizes the concept of conditional execution, takes a string as input, and:
#prints the sentence "Yes - Spathiphyllum is the best plant ever!" to the screen if the inputted string is "Spathiphyllum" (upper-case)
#prints "No, I want a big Spathiphyllum!" if the inputted string is "spathiphyllum" (lower-case)
#prints "Spathiphyllum! Not [input]!" otherwise. Note: [input] is the string taken as input.

print("Lab 3.1.1.10 Comparison operators and conditional execution") #This prints the Lab name to the console
word = input("Write your word here: ") #This takes the variable named word, and prompts the user to assign a string to it

if word == "SPATHIPHYLLUM": #This is the first comparison operation, followed by the conditional execution if it is met
    print("Spathiphyllum is the best plant ever!")
    
elif word == "spathiphyllum": #This comparison operation is conditionally executed if the first comparison operation is not met
    print("No, I want a big Spathiphyllum!")
    
else: #The else statement will always be executed if the previous comparison operations have not been conditionally met
    print("Spathiphyllum! Not",word,"!")
