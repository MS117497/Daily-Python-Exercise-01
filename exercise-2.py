# Michael Spagnola - Python Daily Exercise 2 - 02112018

# 2. Create a program that asks the user to enter their name and their age.
# Print out a message addressed to them that tells them the year that they will turn 100 years old. Clue input()

import datetime

name = raw_input("Enter your name: ")
age = int(raw_input("Enter your age: "))

date = datetime.datetime.today()

year100 = date.year + 100 - age
print name + ', you will be 100 in the year ' + str(year100) + '.'
