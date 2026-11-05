# Module 01 Exercises: Basics

### Exercise 1: Personal Profile
Write a program that stores your name, favorite hobby, and years of coding experience in variables. Print a paragraph using f-strings summarizing this info.

### Exercise 2: Tip Calculator
Ask the user for:
1. Total bill amount (float)
2. Tip percentage (e.g., 15 for 15%)

Calculate and display the tip amount and the final total bill.

---

### Solutions

<details>
<summary>Click to view Exercise 1 Solution</summary>

```python
name = "Alex"
hobby = "photography"
years_exp = 1

print(f"Hi! I'm {name}. I love {hobby} and I have been coding for {years_exp} year(s).")


bill = float(input("Enter total bill: $"))
tip_percent = float(input("Enter tip percentage: "))

tip_amount = bill * (tip_percent / 100)
total = bill + tip_amount

print(f"Tip: ${tip_amount:.2f}")
print(f"Total Bill: ${total:.2f}")