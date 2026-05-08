#Hangman
import random

# Hangman logo
logo = r"""
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/                       
"""

# Hangman stages for 6 lives
stages = [
    """
      +---+
      |   |
      O   |
     /|\\  |
     / \\  |
          ===
""",
    """
      +---+
      |   |
      O   |
     /|\\  |
     /    |
          ===
""",
    """
      +---+
      |   |
      O   |
     /|\\  |
          |
          ===
""",
    """
      +---+
      |   |
      O   |
     /|   |
          |
          ===
""",
    """
      +---+
      |   |
      O   |
      |   |
          |
          ===
""",
    """
      +---+
      |   |
      O   |
          |
          |
          ===
""",
    """
      +---+
      |   |
          |
          |
          |
          ===
"""
]

# Word list
word_list = ["jockey", "python", "banana", "rocket", "garden"]

chosen_word = random.choice(word_list)
word_length = len(chosen_word)

# Display blanks
display = ["_"] * word_length
lives = 6
guessed_letters = []

print(logo)

while lives > 0 and "_" in display:
    print("Word to guess:", "".join(display))
    guess = input("Guess a letter: ").lower()

    # Avoid repeated guesses
    if guess in guessed_letters:
        print(f"You already guessed {guess}. Try another letter.")
        continue

    guessed_letters.append(guess)

    if guess in chosen_word:
        for position in range(word_length):
            if chosen_word[position] == guess:
                display[position] = guess
    else:
        lives -= 1
        print(f"You guessed {guess}, that's not in the word. You lose a life.")

    print(stages[lives])
    print(f"***************{lives}/6 LIVES LEFT***************")

if "_" not in display:
    print(f"YOU WIN! The word was {chosen_word}")
else:
    print(f"IT WAS {chosen_word}! YOU LOSE")