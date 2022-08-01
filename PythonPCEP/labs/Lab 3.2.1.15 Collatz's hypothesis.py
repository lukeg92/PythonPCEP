<<<<<<< HEAD
# take any non-negative and non-zero integer number and name it c0;
# if it's even, evaluate a new c0 as c0 ÷ 2;
# otherwise, if it's odd, evaluate a new c0 as 3 × c0 + 1;
# if c0 ≠ 1, skip to point 2.
# The hypothesis says that regardless of the initial value of c0, it will always go to 1.
# Write a program which reads one natural number and executes the above steps as long as c0 remains different from 1.
# We also want you to count the steps needed to achieve the goal. Your code should output all the intermediate values of c0, too.
# Hint: the most important part of the problem is how to transform Collatz's idea into a while loop - this is the key to success.

# This lab was created by Luke G on 29 Jul 22 at 1545
print("\nLab 3.2.1.15 Collatz's hypothesis\n")

# prompt the user to input a random integer and assign it to variable c0
c0 = int(input("Enter a non negative abd non zero integer here: "))

steps = 0  # Starting the step counter from 0, then increment by 1 every time the body of the whikle loop is executed

while c0 != 1:  # The while conditional loop will execute its body until the sum equals 1

    if c0 % 2 == 0:  # The conditional if statement will execute its body if c0 is even
        c0 /= 2  # In this step in the body, c0 is halved
        steps += 1  # The variable named steps is incremented by 1
        print(int(c0))  # The value of c0 will be printed to the console
# The programme will now go back to the while conditional statement to start the process again

    else:  # This else conditional statement will be met if the value of c0 is not even
        c0 = 3 * c0 + 1  # c0 is multipled by 3 and added by 1
        steps += 1  # The variable named steps is incremented by 1
        print(int(c0))  # The value of c0 will be printed to the console
# The programme will now go back to the while conditional statement to start the process again

# The total number of steps will be output to the console
print("\nsteps =", steps)
=======
# take any non-negative and non-zero integer number and name it c0;
# if it's even, evaluate a new c0 as c0 ÷ 2;
# otherwise, if it's odd, evaluate a new c0 as 3 × c0 + 1;
# if c0 ≠ 1, skip to point 2.
# The hypothesis says that regardless of the initial value of c0, it will always go to 1.
# Write a program which reads one natural number and executes the above steps as long as c0 remains different from 1.
# We also want you to count the steps needed to achieve the goal. Your code should output all the intermediate values of c0, too.
# Hint: the most important part of the problem is how to transform Collatz's idea into a while loop - this is the key to success.

# This lab was created by Luke G on 29 Jul 22 at 1545
print("\nLab 3.2.1.15 Collatz's hypothesis\n")

# prompt the user to input a random integer and assign it to variable c0
c0 = int(input("Enter a non negative abd non zero integer here: "))

steps = 0  # Starting the step counter from 0, then increment by 1 every time the body of the whikle loop is executed

while c0 != 1:  # The while conditional loop will execute its body until the sum equals 1

    if c0 % 2 == 0:  # The conditional if statement will execute its body if c0 is even
        c0 /= 2  # In this step in the body, c0 is halved
        steps += 1  # The variable named steps is incremented by 1
        print(int(c0))  # The value of c0 will be printed to the console
# The programme will now go back to the while conditional statement to start the process again

    else:  # This else conditional statement will be met if the value of c0 is not even
        c0 = 3 * c0 + 1  # c0 is multipled by 3 and added by 1
        steps += 1  # The variable named steps is incremented by 1
        print(int(c0))  # The value of c0 will be printed to the console
# The programme will now go back to the while conditional statement to start the process again

# The total number of steps will be output to the console
print("\nsteps =", steps)
>>>>>>> 8737b48f81813faf037ab2c1d1c58a4e9e948e2b
