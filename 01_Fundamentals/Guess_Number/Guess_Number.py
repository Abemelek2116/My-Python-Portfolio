"""
🎯 Number Guessing Game
-----------------------
A simple Python guessing game where the player tries to guess
a randomly selected number between 1 and 100.

Features:
- Two difficulty modes: Easy (10 turns) and Hard (5 turns)
- Input validation and feedback ("Too high" / "Too low")
- Clear function structure and professional documentation

Author: Abemelek Berhanu
"""

from random import randint

# --- Constants for Game Difficulty ---
EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5


def check_answer(guess: int, answer: int, turns: int) -> int:
    """
    Check the player's guess against the actual answer.
    Returns the number of turns remaining.
    """
    if guess > answer:
        print("Too high.")
        return turns - 1
    elif guess < answer:
        print("Too low.")
        return turns - 1
    else:
        print(f"🎉 You got it! The answer was {answer}.")
        return turns


def set_difficulty() -> int:
    """
    Prompt the user to choose a difficulty level.
    Returns the corresponding number of turns.
    """
    level = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    if level == "easy":
        return EASY_LEVEL_TURNS
    return HARD_LEVEL_TURNS


def game():
    """Main game function — handles setup, user input, and game loop."""
    print(logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    answer = randint(1, 100)

    # Uncomment the next line for debugging/testing:
    # print(f"[DEBUG] The correct answer is {answer}")

    turns = set_difficulty()
    guess = None

    while guess != answer:
        print(f"\nYou have {turns} attempts remaining to guess the number.")
        try:
            guess = int(input("Make a guess: "))
        except ValueError:
            print("⚠️ Please enter a valid number.")
            continue

        turns = check_answer(guess, answer, turns)

        if guess == answer:
            break
        elif turns == 0:
            print(f"💀 You've run out of guesses. The number was {answer}. Better luck next time!")
            return
        else:
            print("Guess again!")


# Entry point
if __name__ == "__main__":
    game()

