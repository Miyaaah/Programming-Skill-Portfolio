# -*- coding: utf-8 -*-
"""
Created on Wed Oct  9 21:18:38 2024

@author: Mia Lovina
"""


answer = (input("What is the capital of France? ")) # Asking and getting input from user

if answer.lower() == "paris":  # Check if the answer matches "paris" regardless of case

    print("Correct! Paris is the capital of France.")

else:      # If the answer is incorrect, inform the user the correct answer
    
    print("Wrong, the answer is Paris.")


