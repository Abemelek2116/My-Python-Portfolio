"""
🎴 Blackjack Game
-----------------
A simple console-based Blackjack game built with Python.
Rules:
- The deck is unlimited in size.
- There are no jokers.
- Jack, Queen, and King all count as 10.
- The Ace can count as 11 or 1.
- The player plays against the computer dealer.
"""

import random


def deal_card():
    """Return a random card from the deck."""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)


def calculate_score(cards):
    """
    Take a list of cards and return the total score.
    Special Rules:
    - A hand with 2 cards summing to 21 (Ace + 10) is a Blackjack (represented by score 0).
    - If the hand contains an Ace (11) and goes over 21, the Ace becomes 1.
    """
    if sum(cards) == 21 and len(cards) == 2:
        return 0  # 0 represents a Blackjack

    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)

    return sum(cards)


def compare(user_score, computer_score):
    """
    Compare user and computer scores and return the game result as a string.
    """
    if user_score > 21 and computer_score > 21:
        return "You both went over. You lose 😤"

    if user_score == computer_score:
        return "Draw 🙃"
    elif computer_score == 0:
        return "Lose, opponent has Blackjack 😱"
    elif user_score == 0:
        return "Win with a Blackjack 😎"
    elif user_score > 21:
        return "You went over. You lose 😭"
    elif computer_score > 21:
        return "Opponent went over. You win 😁"
    elif user_score > computer_score:
        return "You win 😃"
    else:
        return "You lose 😤"


def play_game():
    """Main function that runs a single round of Blackjack."""

    user_cards = []
    computer_cards = []
    is_game_over = False

    # Deal initial two cards to both player and dealer
    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    # Player's turn
    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)

        print(f"Your cards: {user_cards}, current score: {user_score}")
        print(f"Computer's first card: {computer_cards[0]}")

        # End the game if player or dealer has blackjack, or player busts
        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ")
            if user_should_deal == "y":
                user_cards.append(deal_card())
            else:
                is_game_over = True

    # Dealer's turn — draws until score is 17 or more
    computer_score = calculate_score(computer_cards)
    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    # Recalculate user_score to ensure it's always defined
    user_score = calculate_score(user_cards)

    # Display final results
    print(f"\nYour final hand: {user_cards}, final score: {user_score}")
    print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")
    print(compare(user_score, computer_score))


# Game loop — allows user to play multiple rounds
while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
    play_game()
