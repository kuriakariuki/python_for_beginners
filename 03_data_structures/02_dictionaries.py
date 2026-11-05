"""
Module 03: Data Structures
File 02: Dictionaries
--------------------
Dictionaries store key-value pairs.
"""

# Creating a dictionary
student = {
    "name": "Alex",
    "age": 20,
    "courses": ["Math", "Computer Science"],
    "is_enrolled": True
}

# Accessing values
print("Student Name:", student["name"])
print("Courses:", student.get("courses"))

# Adding or updating values
student["grade"] = "A"
student["age"] = 21
print("\nUpdated Student:", student)

# Removing keys
del student["is_enrolled"]

# Iterating through dictionary
print("\nKeys & Values:")
for key, value in student.items():
    print(f"{key}: {value}")