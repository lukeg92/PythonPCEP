<<<<<<< HEAD
# There once was a hat. The hat contained no rabbit, but a list of five numbers: 1, 2, 3, 4, and 5.
# Your task is to:
# write a line of code that prompts the user to replace the middle number in the list with an integer number entered by the user(Step 1)
# write a line of code that removes the last element from the list(Step 2)
# write a line of code that prints the length of the existing list(Step 3).
# Ready for this challenge?

# This lab was created by Luke G on 29 Jul 22 at 1950
print("\nLab 3.4.1.6 The basics of lists\n")

# This is an existing list of numbers hidden in the hat.
hat_list = [1, 2, 3, 4, 5]

# Step 1: write a line of code that prompts the user to replace the middle number with an integer number entered by the user.
# The number input by the user will be assigned to variable user_num
user_num = int(
    input("Enter a new number to replace the middle number in the list: "))
# The third index element in hat_list will be replaced by user_num
hat_list[2] = user_num

# Step 2: write a line of code that removes the last element from the list.
# The del instruction removes the element at the end of the list
del hat_list[-1]

# Step 3: write a line of code that prints the length of the existing list.
print(len(hat_list))

print(hat_list)
=======
# There once was a hat. The hat contained no rabbit, but a list of five numbers: 1, 2, 3, 4, and 5.
# Your task is to:
# write a line of code that prompts the user to replace the middle number in the list with an integer number entered by the user(Step 1)
# write a line of code that removes the last element from the list(Step 2)
# write a line of code that prints the length of the existing list(Step 3).
# Ready for this challenge?

# This lab was created by Luke G on 29 Jul 22 at 1950
print("\nLab 3.4.1.6 The basics of lists\n")

# This is an existing list of numbers hidden in the hat.
hat_list = [1, 2, 3, 4, 5]

# Step 1: write a line of code that prompts the user to replace the middle number with an integer number entered by the user.
# The number input by the user will be assigned to variable user_num
user_num = int(
    input("Enter a new number to replace the middle number in the list: "))
# The third index element in hat_list will be replaced by user_num
hat_list[2] = user_num

# Step 2: write a line of code that removes the last element from the list.
# The del instruction removes the element at the end of the list
del hat_list[-1]

# Step 3: write a line of code that prints the length of the existing list.
print(len(hat_list))

print(hat_list)
>>>>>>> 8737b48f81813faf037ab2c1d1c58a4e9e948e2b
