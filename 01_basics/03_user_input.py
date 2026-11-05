"""
Module 01: Basics
File 03: User Input
------------------
The `input()` function allows your program to receive text from the user.
Note: input() ALWAYS returns data as a String!
"""

# Ask user for their name
user_name = input("Enter your name: ")
print(f"Hello, {user_name}!")

# Getting numbers requires type casting (conversion)
age_str = input("Enter your age: ")
# Convert string to integer using int()
age = int(age_str)

# Perform math with converted value
years_to_100 = 100 - age
print(f"You will turn 100 years old in {years_to_100} years!")