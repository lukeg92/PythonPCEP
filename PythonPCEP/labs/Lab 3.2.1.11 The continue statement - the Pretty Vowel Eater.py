#redesign the (ugly) vowel eater from the previous lab (3.1.2.10)
#create a better, upgraded (pretty) vowel eater! Write a program that uses:
#a for loop;
#the concept of conditional execution (if-elif-else)
#the continue statement.
#ask the user to enter a word;
#use user_word = user_word.upper() to convert the word entered by the user to upper case
#use conditional execution and the continue statement to "eat" the following vowels A, E, I, O, U from the inputted word;
#assign the uneaten letters to the word_without_vowels variable and print the variable to the screen.
#Look at the code in the editor. We've created word_without_vowels and assigned an empty string to it. 
#Use concatenation operation to ask Python to combine selected letters into a longer string during subsequent loop turns, and assign it to the word_without_vowels variable.

#This lab was created by Luke G on 28 Jul 22 at 1600
print("\nLab 3.2.1.11 The continue statement - the Pretty Vowel Eater\n")
word_without_vowels = ""

user_word = input("Enter a word: ")  # Prompt the user to enter a word
user_word = user_word.upper()  # capitalise the letters in the user_word string


for letter in user_word:
    if letter == "A":  # The conditional if statement checks for any letter A in the user_word variable
        continue  # If a letter A is found, the loop will skip the letter and continue through the loop

    elif letter == "E":  # The conditional if statement checks for any letter E in the user_word variable
        continue  # If a letter E is found, the loop will skip the letter and continue through the loop

    elif letter == "I":  # The conditional if statement checks for any letter I in the user_word variable
        continue  # If a letter I is found, the loop will skip the letter and continue through the loop

    elif letter == "O":  # The conditional if statement checks for any letter O in the user_word variable
        continue  # If a letter O is found, the loop will skip the letter and continue through the loop

    elif letter == "U":  # The conditional if statement checks for any letter U in the user_word variable
        continue  # If a letter U is found, the loop will skip the letter and continue through the loop

    else:
        word_without_vowels += letter #This concatenates the consonant letters in the variable user_word to the variable named word_without_vowels

print(word_without_vowels)
