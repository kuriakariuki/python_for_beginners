"""
Mini-Project: Guess the Number
------------------------------
The computer picks a random number between 1 and 100.
The player has to guess it, receiving hints of 'Too High' or 'Too Low'.
"""

import random

def play_game():
    secret_number = random.randint(1, 100)
    attempts = 0
    guessed = False

    print("=== Guess the Number Game ===")
    print("I'm thinking of a number between 1 and 100.")

    while not guessed:
        try:
            user_guess = int(input("Enter your guess: "))
            attempts += 1

            if user_guess < secret_number:
                print("Too LOW! Try again.")
            elif user_guess > secret_number:
                print("Too HIGH! Try again.")
            else:
                guessed = True
                print(f"🎉 Congratulations! You guessed it in {attempts} attempts!")
        except ValueError:
            print("Invalid input! Please enter a valid integer.")

if __name__ == "__main__":
    play_game()