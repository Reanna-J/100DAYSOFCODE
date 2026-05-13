#Blackjack
"""A console-based Blackjack game built using Python. The game follows standard Blackjack rules, where the player competes against the computer to get as close to 21 as possible without going over.

Features:
Random card dealing using random.choice()
Score calculation with Ace (11 or 1) handling
Player can hit (draw a card) or stand (end turn)
Computer follows the standard Blackjack rule (hits until 17 or more)
Automatic winner determination

Game Rules:
The game starts with two cards each for the player and the computer.
The player can choose to hit (draw a card) or stand (end their turn).
The goal is to reach 21 or have a higher score than the computer without exceeding 21.
Aces can be 11 or 1 depending on the score.
The computer draws until it reaches 17 or more."""

import random

def deal_card():
    """Returns a random card from the deck."""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)

def calculate_score(cards):
    """Returns the score for a list of cards."""
    score = sum(cards)

    if score == 21 and len(cards) == 2:
        return 0  # Blackjack

    # Convert Ace from 11 to 1 if score goes over 21
    if 11 in cards and score > 21:
        cards[cards.index(11)] = 1
        score = sum(cards)

    return score

def compare(user_score, computer_score):
    """Compares scores and returns the result."""
    if computer_score == 0:
        return "Lose, opponent has Blackjack 😱"
    elif user_score == 0:
        return "Win with a Blackjack 😎"
    elif user_score > 21:
        return "You went over. You lose 😭"
    elif computer_score > 21:
        return "Opponent went over. You win 😁"
    elif user_score > computer_score:
        return "You win 😃"
    elif user_score < computer_score:
        return "You lose 😤"
    else:
        return "Draw 🙃"

def play_game():
    user_cards = []
    computer_cards = []
    is_game_over = False

    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)

        print(f"\nYour cards: {user_cards}, current score: {user_score}")
        print(f"Computer's first card: {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            user_should_deal = input(
                "Type 'y' to get another card, type 'n' to pass: "
            ).lower()

            if user_should_deal == "y":
                user_cards.append(deal_card())
            else:
                is_game_over = True

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"\nYour final hand: {user_cards}, final score: {user_score}")
    print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")
    print(compare(user_score, computer_score))


while input("\nDo you want to play a game of Blackjack? Type 'y' or 'n': ").lower() == "y":
    print("\n" * 20)
    play_game()