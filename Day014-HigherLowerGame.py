from Day014_gamedata import data
import random

def format_data(account):
    name = account["name"]
    description = account["description"]
    country = account["country"]
    return f"{name}, a {description}, from {country}"


def check_answer(guess, a_followers, b_followers):
    if a_followers > b_followers:
        return guess == "a"
    return guess == "b"


score = 0
game_should_continue = True

account_a = random.choice(data)

while game_should_continue:

    account_b = random.choice(data)

    while account_a == account_b:
        account_b = random.choice(data)

    print(f"Compare A: {format_data(account_a)}")
    print("vs")
    print(f"Against B: {format_data(account_b)}")

    guess = input("Who has more followers? Type 'A' or 'B': ").lower()

    print("\n" * 20)

    a_followers = account_a["follower_count"]
    b_followers = account_b["follower_count"]

    if check_answer(guess, a_followers, b_followers):
        score += 1
        print(f"You're right! Current score: {score}")
        print(f"Use")
        account_a = account_b

    else:
        print(f"Sorry, that's wrong. Final score: {score}")
        game_should_continue = False