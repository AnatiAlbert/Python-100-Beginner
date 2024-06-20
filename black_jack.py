import random
from black_art import logo


def deal_cards():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card


def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0

    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)

    return sum(cards)

def compare(user_score, computer_score):
    if user_score == computer_score:
        return "It's a draw"
    elif user_score == 0:
        return "Blackjack, you've won!"
    elif computer_score == 0:
        return "Opponent has blackjack, you lost!"
    elif user_score > 21:
        return "Over the mark. You lost"
    elif computer_score > 21:
        return "You won!"
    elif user_score > computer_score:
        return "You've won!"
    else:
        return "You lost!"

def play_game():
    print(logo)
    user_card = []
    computer_card = []
    game_over = False

    for _ in range(2):
        user_card.append(deal_cards())
        computer_card.append(deal_cards())

    while not game_over:
        user_score = calculate_score(user_card)
        computer_score = calculate_score(computer_card)

        print(f"   Your hand is: {user_card}, current score: {user_score}")
        print(f"    Computer's first hand is {computer_card[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            game_over = True
        else:
            another_card = input("Do you want to add more cards, type 'y' for yes or 'n' for pass: ")
            if another_card == 'y':
                user_card.append(deal_cards())
            else:
                game_over = True

    while computer_score != 0 and computer_score < 17:
        computer_card.append(deal_cards())
        computer_score = calculate_score(computer_card)

    print(f"    Your final hand: {user_card}. Final score: {user_score}")
    print(f"    Computer's final hand: {computer_card} and final score: {computer_score}")
    print(compare(user_score, computer_score))

start_game = input("Do you want to play a game of blackjack, type 'y' or 'n' for pass: ")
if start_game == 'y':
    play_game()
