alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd',
'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
'u', 'v', 'w', 'x', 'y', 'z']


def caesar(c_text, shift_amount, c_direction):
    end_text = ""
    if c_direction == "decode":
        shift_amount *= -1
    for letter in c_text:
        if letter in alphabet:
            position = alphabet.index(letter)
            new_pos = position + shift_amount
            end_text += alphabet[new_pos]
        else:
            end_text += letter

    print(f"Your {c_direction}d text is {end_text}\n")

from caesar_art import logo
print(logo)

should_continue = True

while should_continue:
    direction = input("Type 'encode' to encrypt and 'decode' to decrypt\n")
    text = input("Type your message here\n")
    shift = int(input("Type your shift amount\n"))

    shift = shift % 26

    caesar(c_text=text, shift_amount=shift, c_direction=direction)

    restart = input("Type 'yes' to restart or 'no' to stop\n")
    if restart == "no":
        should_continue = False
