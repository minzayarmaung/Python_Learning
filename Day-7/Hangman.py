import random
from hangmanpics import stages
from words import word_list

chosen_word = random.choice(word_list)
word_length = len(chosen_word)

print(chosen_word)

lives = 6

from hangmanpics import logo
print(logo)

# Creating Blanks
display = []
for _ in chosen_word:
    display += "_"


end_of_game = False

while not end_of_game:
    guess = input("Guess a Letter: ").lower()

    if guess in display:
        print(f"You have already guessed {guess}.")

    # Guessing
    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    if guess not in chosen_word:
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You Lose!")

    print(" ".join(display))

    if "_" not in display:
        end_of_game = True
        print("You Win!")

    print(stages[lives-1])
