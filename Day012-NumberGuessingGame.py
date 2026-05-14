# Number Guessing Game
import random
print("Welcome to the Number Guessing Game!\n I'm thinking of a number between 1 and 100.")
num = random.randint(1,100)
diff = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
if diff == "easy":
    attempts = 10
else:
    attempts = 5
while attempts > 0:
    print(f"You have {attempts} attempts remaining to guess the number.")
    guess = int(input("Make a guess: "))
    if guess == num:
        print(f"You got it! The answer was {num}.")
        break
    elif guess > num:
        print("Too high.")
    else:
        print("Too low.")
    attempts -= 1
    if attempts == 0:
        print("You've run out of guesses. Refresh the page to run again.")
    else:
        print("Guess again.")