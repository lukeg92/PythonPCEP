# Imagine a list - not very long, not very complicated, just a simple list containing some integer numbers.
# Some of these numbers may be repeated, and this is the clue. We don't want any repetitions. We want them to be removed.
# Your task is to write a program which removes all the number repetitions from the list.
# The goal is to have a list in which all the numbers appear not more than once.
# Note: assume that the source list is hard-coded inside the code - you don't have to enter it from the keyboard.
# Of course, you can improve the code and add a part that can carry out a conversation with the user and obtain all the data from her/him.
# Hint: we encourage you to create a new list as a temporary work area - you don't need to update the list in situ.
# We've provided no test data, as that would be too easy. You can use our skeleton instead.

# This lab was created by Luke G on 1 Aug 22 at 2000
print("\nLab 3.6.1.9 Operating with lists - basics\n")

# This variable assigned the name my_list is the list of integers that will be the subject of the programme
my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]

non_repetitive_list = []  # This variable named non_repetitive_list is an empty list that acts as a placeholder in which the for conditional loop will insert integers

for number in my_list:  # The for conditional loop will check each element in turn from the my_list variable
    if number not in non_repetitive_list:  # This line looks at the numer in my_list and checks to see if that number is not in non_repetitive_list too
        # If the number is not in non_repetitive_list, the number will be appended to non_repetitive_list
        non_repetitive_list.append(number)
    # If the condition above was not met (The number is already in non_repetitive_list) follow this step
    else:
        continue  # The continue keyword prompts the programme to move onto the next line within the loop's body

# This ouputs the non_repetitive_list
print("The list with unique elements only:", non_repetitive_list)
print(my_list)
