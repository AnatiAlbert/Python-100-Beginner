import random
from hangman_art import stages, logo
from hangman_words import word_list

chosen_word = random.choice(word_list)
word_length = len(chosen_word)
print(chosen_word)

lives = 6
end_of_game = False
display = []

for _ in range(word_length):
    display += "_"

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    if guess in display:
        print(f"You've already guessed {guess}")

    for position in range(word_length):
        letter = chosen_word[position]

        if letter == guess:
            display[position] = letter

    if guess not in chosen_word:
        print(f"You've guessed {guess} not in word. You've lost a life!")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You've lost!")

    print(f"{''.join(display)}")

    print(stages[lives])

    if "_" not in display:
        end_of_game = True
        print("You win!")
