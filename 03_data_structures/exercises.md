# Module 03 Exercises: Data Structures

### Exercise 1: Unique Word Counter
Given a sentence, convert it into a list of words, then use a `set` to count how many **unique** words were used.

### Exercise 2: Inventory Checker
Create a dictionary representing store inventory (item name -> quantity). Prompt the user for an item name and return its quantity. If it's not in the dictionary, inform the user it's out of stock.

---

### Solutions

<details>
<summary>Click to view Exercise 1 Solution</summary>

```python
sentence = "python is great and python is easy to learn"
words = sentence.split()
unique_words = set(words)
print(f"Total words: {len(words)}")
print(f"Unique words count: {len(unique_words)}")


inventory = {"apples": 10, "bananas": 5, "oranges": 0}
item = input("Search item: ").lower()

if item in inventory and inventory[item] > 0:
    print(f"{item.capitalize()} available: {inventory[item]}")
else:
    print(f"Sorry, {item} is out of stock.")