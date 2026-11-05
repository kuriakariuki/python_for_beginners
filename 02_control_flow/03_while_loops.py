"""
Module 02: Control Flow
File 03: While Loops
--------------------
While loops keep running as long as a condition evaluates to True.
"""

print("--- 1. Basic While Loop ---")
countdown = 5
while countdown > 0:
    print(f"T-minus {countdown}...")
    countdown -= 1
print("Blastoff! 🚀")

print("\n--- 2. Using break and continue ---")
# Keep asking for input until the user types 'exit'
while True:
    user_input = input("Type 'exit' to stop: ")
    if user_input.lower() == 'exit':
        print("Exiting loop...")
        break
    elif user_input == "":
        print("You typed nothing, skipping...")
        continue
    print(f"You typed: {user_input}")