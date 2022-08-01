#Run the program to play the Guess the secret number game, and guess the secret number. 
#Those who don't guess the number will be stuck in an endless loop forever! 
#Your task is to complete the code in the editor in such a way so that the code:
#will ask the user to enter an integer number;
#will use a while loop;
#will check whether the number entered by the user is the secret number. 
#If the number chosen by the user is different than the secret number, the user should see the message:
#"Ha ha! You're stuck in my loop!" and be prompted to enter a number again. 
#If the number entered by the user matches the secret number, the number should be printed to the screen, and the console should say the following words: 
#"Well done, muggle! You are free now."

#This lab was created by Luke G on 28 Jul 22 at 1430
print("\nLab 3.2.1.3 Essentials of the while loop - Guess the secret number")

secret_number = 777

print(
"""
+================================+
| Welcome to my game, muggle!    |
| Enter an integer number        |
| and guess what number I've     |
| picked for you.                |
| So, what is the secret number? |
+================================+
""")

num = int(input("Enter your number here: ")) #This prompts the user to input their first integer and assigns it to the variable named num

while num != 777: #The while conditional statement checks if the variable named num is not equal to 777.
                  #If the num variable is not equal to 777, the code inside the while loop will be executed
    print("\nHa ha! You're stuck in my loop!") #The print function outputs the string to the console
    num = int(input("\nTry another number: ")) #The code remains inside the while loop and prompts the user to input another integer
                                  #The code will return to the start of the while loop until the condition is met.

print("\nWell done, muggle! You are free now.") #The print function will output the string when the user inputs num 777

