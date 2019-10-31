"""
Programmer: Faith Goodman
Date: 10.15.19
Program: Double For Loop

This program will nest a for loop inside another for loop.
"""
for i in range(3):
    print("Outer For Loop: " + str(i))
    for y in range(2):
<<<<<<< Updated upstream
        print("   Inner For Loop: " + str(y))
=======
        print("   Inner For Loop: " + str(y))

print("\n                                                                  \n")

"""
Programmer: Faith Goodman
Date: 10.23.19
Program: For Loop plus While Loop

This program will create a For Loop with a While Loop embedded into it
"""
for i in range(4):
    print("Outer For Loop: " + str(i))
    x = 5
    while x >= 0:
        print("         While Loop: " + str(x))
        x = x - 1
