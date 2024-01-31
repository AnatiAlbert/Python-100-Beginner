import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''


symbols = [rock, paper, scissors]

print("Choose your choice. Type 0 for ROCK, 1 for PAPER and 2 for SCISSORS\n")
user_choice = int(input())
if user_choice >= 3 or user_choice < 0:
    print("Invalid number, You lose")
else:
    print(f"Your number is: {user_choice}")
    print(symbols[user_choice])
    computer_choice = random.randint(0, 2)
    print(f"Computer's number is {computer_choice}")
    print(symbols[computer_choice])

    if user_choice == 0 and computer_choice == 2:
        print("You win!")
    elif computer_choice == 0 and user_choice == 2:
        print("You lose.")
    elif user_choice > computer_choice:
        print("You win!")
    elif computer_choice > user_choice:
        print("You lose.")
    elif user_choice == computer_choice:
        print("Draw, try again!")
