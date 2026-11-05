"""
Module 03: Data Structures
File 01: Lists
--------------
Lists are ordered, mutable collections of elements.
"""

# Creating a list
fruits = ["apple", "banana", "cherry"]
print("Original List:", fruits)

# Accessing elements (0-indexed)
print("First fruit:", fruits[0])
print("Last fruit:", fruits[-1])

# Modifying items
fruits[1] = "blueberry"
print("Modified List:", fruits)

# Adding elements
fruits.append("orange")        # Add to end
fruits.insert(1, "mango")      # Insert at specific index
print("After Adding:", fruits)

# Removing elements
fruits.remove("cherry")        # Remove by value
popped_item = fruits.pop()     # Remove last item and return it
print("After Removals:", fruits)
print("Popped item:", popped_item)

# Loop through list
print("\nIterating over fruits:")
for fruit in fruits:
    print(f"- {fruit.capitalize()}")