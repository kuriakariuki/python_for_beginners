"""
Module 03: Data Structures
File 03: Tuples and Sets
-----------------------
- Tuples: Ordered, IMMUTABLE (cannot be changed).
- Sets: Unordered, unique items only.
"""

# 1. TUPLES (Parentheses)
coordinates = (37.7749, -122.4194)
print("Coordinates:", coordinates)
print("Latitude:", coordinates[0])
# coordinates[0] = 40.0  # ❌ This will throw an Error! Tuples cannot be modified.

# 2. SETS (Curly Brackets)
unique_numbers = {1, 2, 3, 3, 4, 4, 5}
print("\nUnique Numbers Set (duplicates automatically removed):", unique_numbers)

unique_numbers.add(6)
unique_numbers.remove(1)
print("Updated Set:", unique_numbers)

# Set Operations
set_a = {1, 2, 3}
set_b = {3, 4, 5}
print("Union:", set_a | set_b)
print("Intersection:", set_a & set_b)
