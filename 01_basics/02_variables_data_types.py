"""
Module 01: Basics
File 02: Variables and Data Types
---------------------------------
Variables store data values in memory.
Python automatically understands the type of data you assign to a variable.
"""

# 1. Integers (Whole numbers)
age = 25
year = 2026
print("Age:", age)
print("Data type of age:", type(age))

# 2. Floats (Decimals)
price = 19.99
pi = 3.14159
print("\nPrice:", price)
print("Data type of price:", type(price))

# 3. Strings (Text)
name = "Alice"
greeting = 'Hello, Python learner!'
print("\nName:", name)
print("Data type of name:", type(name))

# 4. Booleans (True or False)
is_learning = True
is_finished = False
print("\nIs learning?", is_learning)
print("Data type of is_learning:", type(is_learning))

# 5. String Concatenation & Formatting
full_greeting = greeting + " My name is " + name
print("\nConcatenated String:", full_greeting)

# F-strings (Modern way to embed variables in strings)
print(f"F-String Example: {name} is {age} years old.")