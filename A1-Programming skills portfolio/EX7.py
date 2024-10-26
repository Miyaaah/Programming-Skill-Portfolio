# -*- coding: utf-8 -*-
"""
Created on Sun Oct 13 12:33:34 2024

@author: Mia Lovina
"""
print("Numbers counting from 0 to 50:")
# Count from 0 to 50 inclusive. The range goes from 0 to 51 to include 50
for x in range(0, 51):
    print(x) 

print("Numbers counting 50 down to 0:")
# Count down from 50 to 0 inclusive. The range goes from 50 to -1 to include 0
#To reverse the count the range would be (Start, Stop, Step). -1 to make a number go down
for a in range(50, -1, -1):
    print(a) 

print("Numbers counting 30 to 50:")
# Count from 30 to 50 inclusive. The range goes from 30 to 51 to include 50
for a in range(30, 51):
    print(a) 

print("Numbers counting 50 down to 10:")
# Count down from 50 to 10 inclusive, decrementing by 2 each time
# The range goes from 50 to 9 to include 10
for a in range(50, 9, -2):
    print(a) 

print("Numbers counting 100 to 200:")
# Count from 100 to 200 inclusive, incrementing by 5 each time
# The range goes from 100 to 201 to include 200.
for a in range(100, 201, 5):
    print(a)