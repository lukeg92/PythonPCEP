#The break statement is used to exit/terminate a loop.
#Design a program that uses a while loop and continuously asks the user to enter a word unless the user enters "chupacabra" as the secret exit word
#in which case the message "You've successfully left the loop." should be printed to the screen, and the loop should terminate.

#This lab was created by Luke G on 28 Jul 22 at 1520
print("\nLab 3.2.1.9 The break statement - Stuck in a loop\n")
while 1: #This conditional statement creates a while loop. While the loop's body is true, the loop will execute. 1 could be replaced with True for less ambiguity
    word = input("Guess a word: ") #This prompts the user to input a string which will be assigned to the variable named word
    if word == "chupacabra": #If the guessed word is chupacabra, the next line will be executed, and the loop will break
        break #This prompts the loop to break
        
    else: #If the guessed word is not chupacabra, the else conditional statement will be executed
        word = input("Guess a word: ") #This prompts the user to input a new string, which will be assigned to (and replace) the variable named word
        
print("You've successfully left the loop.") #Once the conditional while statement is met, and the break statement is met, this line will be output to the console
        
