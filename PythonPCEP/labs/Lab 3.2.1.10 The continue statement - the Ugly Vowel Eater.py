#The continue statement is used to skip the current block and move ahead to the next iteration, without executing the statements inside the loop.
#It can be used with both the while and for loops.
#Design a vowel eater! Write a program that uses:
#a for loop;
#the concept of conditional execution (if-elif-else)
#the continue statement.
#Your program must:
#ask the user to enter a word;
#use conditional execution and the continue statement to "eat" the following vowels A, E, I, O, U from the inputted word;
#print the uneaten letters to the screen, each one of them on a separate line.

#This lab was created by Luke G on 28 Jul 22 at 1530
print("\nLab 3.2.1.10 The continue statement - the Ugly Vowel Eater\n")
user_word = input("Enter a word: ")  # Prompt the user to enter a word
user_word = user_word.upper() #capitalise the letters in the user_word string

for letter in user_word: #The conditional for statement begins the for loop and assigns letter as the control variable

    if letter == "A": #The conditional if statement checks for any letter A in the user_word variable
        continue #If a letter A is found, the loop will skip the letter and continue through the loop
        
    elif letter == "E": #The conditional if statement checks for any letter E in the user_word variable
        continue #If a letter E is found, the loop will skip the letter and continue through the loop
        
    elif letter == "I": #The conditional if statement checks for any letter I in the user_word variable
        continue #If a letter I is found, the loop will skip the letter and continue through the loop
        
    elif letter == "O": #The conditional if statement checks for any letter O in the user_word variable
        continue #If a letter O is found, the loop will skip the letter and continue through the loop
        
    elif letter == "U": #The conditional if statement checks for any letter U in the user_word variable
        continue #If a letter U is found, the loop will skip the letter and continue through the loop
        
    print(letter) #Complete the body of the for loop. All other letters will be printed to the console on separate lines
