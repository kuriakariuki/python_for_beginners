# Module 02 Exercises: Control Flow

### Exercise 1: Even or Odd
Write a script that asks the user for an integer and prints whether the number is **even** or **odd**.

### Exercise 2: Multiplication Table
Prompt the user for a number, then use a `for` loop to print its multiplication table from 1 to 10.

---

### Solutions

<details>
<summary>Click to view Exercise 1 Solution</summary>

```python
num = int(input("Enter a number: "))
if num % 2 == 0:
    print(f"{num} is Even.")
else:
    print(f"{num} is Odd.")


num = int(input("Enter a number for table: "))
for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")