#Write a program that uses a for loop to "count mississippily" to five. 
#Having counted to five, the program should print to the screen the final message "Ready or not, here I come!"

#This lab was created by Luke G on 28 Jul 22 at 1500
print("Lab 3.2.1.6 Essentials of the for loop - counting mississippily")
import time #In Python, you use the import keyword to make code in one module available in another.

for count in range(1,6): #This conditional for loop takes the control variable "count" to automatically count the loops in the range from 1 - 6 (finishing at 5)
    print(count,"Mississippi") #Whilst the control variable is within the loop, the print function will execute this code
    time.sleep(1) #Still within the loop, an increment of 1 second will be added
    
print("\nReady or not, here I come!") #Once the control variable has met the conditional for loop, this print function will output to the console
