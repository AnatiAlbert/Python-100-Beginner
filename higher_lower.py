from game_art import logo, vs
from game_data import data
import random


def format_data(account):
    name = account['name']
    description = account['description']
    country = account['country']
    return f"{name}, a {description}, from {country}."

def check_answer(guess, a_follower, b_follower):
    if a_follower > b_follower:
        return guess == 'a'
    else:
        return guess == 'b'


game_continue = True
account_b = random.choice(data)
score = 0

while game_continue:
    account_a = account_b
    account_b = random.choice(data)
    while account_a == account_b:
        account_b = random.choice(data)

    print(logo)
    print(f"Compare A: {format_data(account_a)}")
    print(vs)
    print(f"Against B: {format_data(account_b)}")

    guess = input("Who has more followers? Type 'A' or 'B': ").lower()

    a_follower = account_a['follower_count']
    b_follower = account_b['follower_count']
    is_correct = check_answer(guess, a_follower, b_follower)


    if is_correct:
        score += 1
        print(f"You're right. Current score: {score}\n")
    else:
        game_continue = False
        print(f"You're wrong. Final score: {score}\n\n")
