# Opdracht 1
# Create a program that asks the user to enter their name and their age. 
# Print out a message addressed to them that tells them the year that 
# they will turn 100 years old. Note: for this exercise, the expectation 
# is that you explicitly write out the year (and therefore be out of date 
# the next year).

name = input("What is your name: ")
age = int(input("What is your age: "))
CurrentYear = int(input("What is your current year: "))
Math = CurrentYear + 100 - age

print("Age right now: " + str(age))
print(name + " turns 100 in the year " + str(Math))











