"""
Mini-Project: Rock, Paper, Scissors
-----------------------------------
Play Rock, Paper, Scissors against the computer.
"""

import random

def play():
    choices = ["rock", "paper", "scissors"]
    
    print("=== Rock, Paper, Scissors ===")
    user_choice = input("Choose rock, paper, or scissors: ").lower()
    
    if user_choice not in choices:
        print("Invalid choice! Please choose rock, paper, or scissors.")
        return

    computer_choice = random.choice(choices)
    print(f"Computer chose: {computer_choice}")

    # Tie Condition
    if user_choice == computer_choice:
        print("It's a tie!")
    # User Winning Conditions
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "paper" and computer_choice == "rock") or \
         (user_choice == "scissors" and computer_choice == "paper"):
        print("🎉 You Win!")
    else:
        print("💻 Computer Wins!")

if __name__ == "__main__":
    play()