<<<<<<< HEAD
# This lab was created by Luke G on 29 Jul 22 at 2030
from turtle import st


print("\nLab 3.4.1.13 The basics of lists - the Beatles\n")

# step 1: create an empty list named beatles;
beatles = []  # This has created an empty list inside the square brackets and assigned it to the variable named beatles
# The print function will output an empty list to the console
print("Step 1:", beatles)

# step 2: use the append() method to add the following members of the band to the list: John Lennon, Paul McCartney, and George Harrison;
# The beatles.append() method will add the string "John Lennon" to the right of the list
beatles.append("John Lennon")
# The beatles.append() method will add the string "Paul McCartney" to the right of the list
beatles.append("Paul McCartney")
# The beatles.append() method will add the string "George Harrison" to the right of the list
beatles.append("George Harrison")
# The print function will output the names of the beatles to the console
print("Step 2:", beatles)

# step 3: use the for loop and the append() method to prompt the user to add the following members of the band to the list:
# Stu Sutcliffe, and Pete Best;
for i in range(2):  # This will complete the for conditional statement twice
    # This prompts the user to input a new band member
    beatles_member = input("Insert band member: ")
    beatles.append(beatles_member)  # This adds the new band member to the list
print("Step 3:", beatles)

# step 4: use the del instruction to remove Stu Sutcliffe and Pete Best from the list;
# The del keyword and the [-1] prompts the programme to delete the last value in the list (Pete)
del beatles[-1]
# The del keyword and the [-1] prompts the programme to delete the last value in the list (Stu)
del beatles[-1]
print("Step 4:", beatles)

# step 5: use the insert() method to add Ringo Starr to the beginning of the list.
# The insert keyword allows you to choose the position within the list. Position 0 inserts the value "Ringo Starr at the beginning."
beatles.insert(0, "Ringo Star")
print("Step 5:", beatles)


# testing list legth
# The len function will output the length of the beatles list, which is 4 in this programme
print("The Fab", len(beatles))
=======
# This lab was created by Luke G on 29 Jul 22 at 2030
from turtle import st


print("\nLab 3.4.1.13 The basics of lists - the Beatles\n")

# step 1: create an empty list named beatles;
beatles = []  # This has created an empty list inside the square brackets and assigned it to the variable named beatles
# The print function will output an empty list to the console
print("Step 1:", beatles)

# step 2: use the append() method to add the following members of the band to the list: John Lennon, Paul McCartney, and George Harrison;
# The beatles.append() method will add the string "John Lennon" to the right of the list
beatles.append("John Lennon")
# The beatles.append() method will add the string "Paul McCartney" to the right of the list
beatles.append("Paul McCartney")
# The beatles.append() method will add the string "George Harrison" to the right of the list
beatles.append("George Harrison")
# The print function will output the names of the beatles to the console
print("Step 2:", beatles)

# step 3: use the for loop and the append() method to prompt the user to add the following members of the band to the list:
# Stu Sutcliffe, and Pete Best;
for i in range(2):  # This will complete the for conditional statement twice
    # This prompts the user to input a new band member
    beatles_member = input("Insert band member: ")
    beatles.append(beatles_member)  # This adds the new band member to the list
print("Step 3:", beatles)

# step 4: use the del instruction to remove Stu Sutcliffe and Pete Best from the list;
# The del keyword and the [-1] prompts the programme to delete the last value in the list (Pete)
del beatles[-1]
# The del keyword and the [-1] prompts the programme to delete the last value in the list (Stu)
del beatles[-1]
print("Step 4:", beatles)

# step 5: use the insert() method to add Ringo Starr to the beginning of the list.
# The insert keyword allows you to choose the position within the list. Position 0 inserts the value "Ringo Starr at the beginning."
beatles.insert(0, "Ringo Star")
print("Step 5:", beatles)


# testing list legth
# The len function will output the length of the beatles list, which is 4 in this programme
print("The Fab", len(beatles))
>>>>>>> 8737b48f81813faf037ab2c1d1c58a4e9e948e2b
