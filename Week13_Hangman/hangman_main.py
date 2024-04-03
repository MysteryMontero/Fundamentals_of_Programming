import random

from hangman_ascii import stages, logo
from words import words

print(logo)

# words = ['gum', 'flower', 'dice', 'tears', 'tabulation', 'memoization', 'angel', 'devil']
chosen_word = random.choice(words).lower()
len_word = len(chosen_word)
# print(chosen_word)
word_display = []
for _ in range(len_word):
    word_display.append('_')
print(word_display)
game_over = False
incorrect_guess = []
lives_left = 7



while not game_over: # while not is True
    guessed_letter = input('Guess a letter: ').lower()
    if guessed_letter in word_display or guessed_letter in incorrect_guess:
        print(f'You have already guessed {guessed_letter}. Try again!')
        print(f"You have {lives_left} lives left.")
    elif guessed_letter not in chosen_word:
        print(f"Your guess '{guessed_letter}' is WRONG!!!")
        lives_left -= 1 # Same formula as lives_left = lives_left -1
        print(f"You have {lives_left} lives left.")
        incorrect_guess.append(guessed_letter) # Keeps track of letters already guessed.

        if lives_left == 0:
            game_over = True
            print('Game Over. You just hanged a man.')
            print(f"The word was {chosen_word}")
    else:
        for idx, val in enumerate(chosen_word): # Clears off both the value and index.
            if val == guessed_letter:
                word_display[idx] = guessed_letter
    print(word_display)
    if '_' not in word_display:
        game_over = True
        print("Game Over. You win!")
    print(stages[lives_left]) # Takes from hangman_ascii and imports the hang man.


