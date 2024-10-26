# -*- coding: utf-8 -*-
"""
Created on Wed Oct  9 23:31:25 2024

@author: Mia Lovina
"""
"""Advanced Version of Exercise 4"""

#  List of questions and their corresponding answers
questions = [
    {"question": "1. What is the capital of France?", "answer": "paris"},
    {"question": "2. What is the capital of Switzerland?", "answer": "bern"},
    {"question": "3. What is the capital of Netherlands?", "answer": "amsterdam"},
    {"question": "4. What is the capital of United Kingdom?", "answer": "london"},
    {"question": "5. What is the capital of Germany?", "answer": "berlin"},
    {"question": "6. What is the capital of Austria?", "answer": "vienna"},
    {"question": "7. What is the capital of Greece?", "answer": "athens"},
    {"question": "8. What is the capital of Ireland?", "answer": "dublin"},
    {"question": "9. What is the capital of Italy?", "answer": "rome"},
    {"question": "10. What is the capital of Sweden?", "answer": "stockholm"},
    ]

# Using for to loop through each question in the questions list
for q in questions:
 
    user_answer = input(q["question"] + " ")   # Ask the user the current question and store their answer in the same line
    

    if user_answer.lower() == q["answer"]: # Check if the user's answer matches the correct answer without being case sensitive
        print("Correct! The answer is", q["answer"].capitalize()) # If correct, print a message with the correct answer with the proper name
    else: # If incorrect, print a message with the correct answer with the proper name
        print("Wrong! The correct answer is", q["answer"].capitalize())