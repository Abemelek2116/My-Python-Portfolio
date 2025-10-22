"""
Password Generator
------------------
Author: Abemelek Berhanu

A simple password generator that creates secure, randomized passwords
based on user preferences for letters, numbers, and symbols.
"""

import random

# Character sets
LETTERS = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
    'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
    'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
]
NUMBERS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
SYMBOLS = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

def generate_password(nr_letters: int, nr_symbols: int, nr_numbers: int) -> str:
    """
    Generates a random password containing a mix of letters, symbols, and numbers.

    Args:
        nr_letters (int): Number of letters in the password.
        nr_symbols (int): Number of symbols in the password.
        nr_numbers (int): Number of numbers in the password.

    Returns:
        str: A randomized, secure password string.
    """
    password_chars = (
        random.choices(LETTERS, k=nr_letters) +
        random.choices(SYMBOLS, k=nr_symbols) +
        random.choices(NUMBERS, k=nr_numbers)
    )

    # Shuffle to randomize order
    random.shuffle(password_chars)
    return "".join(password_chars)


def main():
    """Main program loop."""
    print("Welcome to the Python Password Generator! 🔐")
    nr_letters = int(input("How many letters would you like in your password? "))
    nr_symbols = int(input("How many symbols would you like? "))
    nr_numbers = int(input("How many numbers would you like? "))

    password = generate_password(nr_letters, nr_symbols, nr_numbers)
    print(f"\nYour generated password is: {password}")


if __name__ == "__main__":
    main()

