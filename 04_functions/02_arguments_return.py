"""
Module 04: Functions
File 02: Arguments and Return Values
-----------------------------------
Functions use `return` to send data back to the caller.
"""

def add(a, b):
    return a + b

def calculate_stats(numbers):
    """Returns multiple values as a tuple."""
    total = sum(numbers)
    average = total / len(numbers)
    return total, average

# Using returned values
result = add(15, 25)
print(f"15 + 25 = {result}")

scores = [88, 92, 79, 95, 100]
total_score, avg_score = calculate_stats(scores)
print(f"Total: {total_score}, Average: {avg_score:.2f}")