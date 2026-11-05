"""
Mini-Project: Simple Calculator
-------------------------------
A terminal-based calculator supporting Addition, Subtraction,
Multiplication, and Division.
"""

def add(x, y): return x + y
def subtract(x, y): return x - y
def multiply(x, y): return x * y
def divide(x, y):
    if y == 0:
        return "Error: Division by zero!"
    return x / y

def calculator():
    print("=== Terminal Calculator ===")
    print("1. Add\n2. Subtract\n3. Multiply\n4. Divide")

    choice = input("Choose operation (1-4): ")

    if choice in ['1', '2', '3', '4']:
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            if choice == '1':
                print(f"Result: {num1} + {num2} = {add(num1, num2)}")
            elif choice == '2':
                print(f"Result: {num1} - {num2} = {subtract(num1, num2)}")
            elif choice == '3':
                print(f"Result: {num1} * {num2} = {multiply(num1, num2)}")
            elif choice == '4':
                print(f"Result: {num1} / {num2} = {divide(num1, num2)}")
        except ValueError:
            print("Invalid input! Please enter numbers only.")
    else:
        print("Invalid operation selection.")

if __name__ == "__main__":
    calculator()