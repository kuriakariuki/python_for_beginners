# Module 04 Exercises: Functions

### Exercise 1: Temperature Converter
Write a function `celsius_to_fahrenheit(celsius)` that converts Celsius temperature to Fahrenheit using formula: `(C * 9/5) + 32`.

### Exercise 2: Palindrome Checker
Write a function `is_palindrome(text)` that returns `True` if a word is spelled the same backward (e.g. "radar", "racecar").

---

### Solutions

<details>
<summary>Click to view Exercise 1 Solution</summary>

```python
def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

print(celsius_to_fahrenheit(0))   # 32.0
print(celsius_to_fahrenheit(100)) # 212.0


def is_palindrome(text):
    clean_text = text.lower().replace(" ", "")
    return clean_text == clean_text[::-1]

print(is_palindrome("racecar")) # True
print(is_palindrome("python"))  # False
