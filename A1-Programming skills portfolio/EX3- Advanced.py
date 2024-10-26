# -*- coding: utf-8 -*-
"""
Created on Sun Oct 13 15:46:29 2024

@author: Mia Lovina
"""


#Exercise 3 Advanced version


# Asking the user to input their name, hometown, and age
student_info = {'name': input("Enter your name: "),
                'hometown': input("Enter your hometown: "),}

while True:
    # Using the try and except method to handle errors
    try: 
        age = int(input("Enter your age: "))
        student_info['age'] = age  # After user defines this it will be added in the dictionary
        break # To get out of the loop if they enter their age as numbers
    except:
        print("Please type numbers as your age.")


# Printing the information on separate lines
print( student_info['name'], student_info['hometown'], student_info['age'], sep='\n')


"""Try giving both your first and second name when asked for your name. 
What happens?

- It will still displays both your first and second name.


How can you handle multiple words in Python?

-In this context users can input multiple words, such their first and last names,
 because Python's input() function captures the input as a single string."

Test the program by entering a string value for age (e.g., "twenty"). 
What happens? How can you prevent this issue?

-I used the try and except blocks so it can let the user know to write their age
as integers instead of words. If the user enters a string like 'twenty', 
the program will tell them to enter integers as their age. """