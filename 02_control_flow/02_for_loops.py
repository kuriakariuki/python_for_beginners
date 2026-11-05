"""
Module 02: Control Flow
File 02: For Loops
------------------
For loops iterate over sequences (ranges, lists, strings).
"""

print("--- 1. Repeating with range() ---")
# range(start, stop_before, step)
for i in range(1, 6):
    print(f"Count: {i}")

print("\n--- 2. Iterating over a string ---")
word = "Python"
for letter in word:
    print(letter.upper())

print("\n--- 3. Calculating a sum ---")
total = 0
for number in range(1, 11): # Sum numbers 1 through 10
    total += number
print(f"Sum of 1 to 10 is: {total}")