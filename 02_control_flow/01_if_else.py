"""
Module 02: Control Flow
File 01: If-Else Statements
---------------------------
Conditionals let your code make decisions based on rules.
"""

score = float(input("Enter your exam score (0-100): "))

# Logical branching with if, elif (else if), and else
if score >= 90:
    grade = 'A'
elif score >= 80:
    grade = 'B'
elif score >= 70:
    grade = 'C'
elif score >= 60:
    grade = 'D'
else:
    grade = 'F'

print(f"Your grade is: {grade}")

# Boolean logic operators: and, or, not
if score >= 60 and score <= 100:
    print("Status: Passed")
else:
    print("Status: Failed or Invalid Score")