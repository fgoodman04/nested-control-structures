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

print("\n                                       \n")

"""
Programmer: Faith Goodman
Date: 10.22.19
Program: Average Test Score

This program asks for the test scores for multiple people and reports
 the average test score for each portion
"""

people = int(input("How many people are taking the test?: "))
test = int(input("How many tests are going to be averaged?: "))

for i in range(people):
    name = input("Enter name: ")
    sum = 0
    for l in range(test):
        score = int(input("Enter a score: "))
        sum = sum + score
    average = float(sum) / test
    print("Average for " + name + ";" + str(round(average, 2)))
