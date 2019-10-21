"""
Programmer: Faith Goodman
Date: 10.15.19
Program: Double For Loop

This program will nest a for loop inside another for loop.
"""
for i in range(3):
    print("Outer For Loop: " + str(i))
    for y in range(2):
        print("   Inner For Loop: " + str(y))