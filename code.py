# This is a simple number guessing game where the user has to guess a randomly generated number.

import random

def guess_number_game():
    """
    This function implements a number guessing game.
    It generates a random number and asks the user to guess it.
    The user is given a limited number of attempts to guess the number.
    """
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    secret_number = random.randint(1, 100)
    attempts = 0
    max_attempts = 5

    while attempts < max_attempts:
        try:
            guess = int(input("Enter your guess: "))
            if guess < secret_number:
                print("Too low! Try a higher number.")
            elif guess > secret_number:
                print("Too high! Try a lower number.")
            else:
                print(f"Congratulations! You guessed the number {secret_number} correctly!")
                break
            attempts += 1
            print(f"You have {max_attempts - attempts} attempts remaining.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    if attempts == max_attempts:
        print(f"Sorry, you've run out of attempts. The number was {secret_number}.")

# Start the game
guess_number_game()
