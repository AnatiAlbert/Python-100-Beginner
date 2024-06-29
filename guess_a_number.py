import random
from guess_art import logo

EASY_LEVEL = 10
HARD_LEVEL = 5

turns = 0

def check_answer(guess, answer, turns):
    if guess < answer:
        print("Too Low.")
        return turns - 1
    elif guess > answer:
        print("Too High.")
        return turns - 1
    else:
        print(f"You have got it. Final answer was {answer}")

def difficulty():
    level = input("Choose a difficulty level. Type 'easy' or 'hard': ")
    if level == 'easy':
        return EASY_LEVEL
    elif level == 'hard':
        return HARD_LEVEL

def game():
    print(logo)
    guess = 0
    answer = random.randint(1, 100)

    print("Welcome to the The Guessing Game!")
    print("Choose a number between 1 to 100")
    #print(f"Final answer is {answer}")

    turns = difficulty()

    while guess != answer:
        print(f"You have {turns} attempts remaining.")
        guess = int(input("Make a guess: "))
        turns = check_answer(guess, answer, turns)
        if turns == 0:
            print("You have lost.")
            return
        elif guess != answer:
            print("Guess again.")

game()
