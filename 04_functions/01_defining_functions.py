"""
Module 04: Functions
File 01: Defining Functions
---------------------------
Functions organize reusable blocks of code.
"""

# Simple function with no arguments
def greet_user():
    print("Welcome to Python Functions!")

# Function with parameters
def say_hello(name):
    print(f"Hello, {name}!")

# Function with default parameters
def greet_with_time(name, time_of_day="morning"):
    print(f"Good {time_of_day}, {name}!")

# Calling functions
greet_user()
say_hello("Charlie")
greet_with_time("Dana")
greet_with_time("Eve", "evening")