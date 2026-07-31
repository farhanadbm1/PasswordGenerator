import random
import string


def generate_password(length, use_letters, use_numbers, use_symbols):
    characters = ""

    if use_letters:
        characters += string.ascii_letters

    if use_numbers:
        characters += string.digits

    if use_symbols:
        characters += string.punctuation

    if not characters:
        return None

    password = ""

    for _ in range(length):
        password += random.choice(characters)

    return password


print("===== Password Generator =====")

length = int(input("Enter password length: "))

letters = input("Include letters? (y/n): ").lower() == "y"
numbers = input("Include numbers? (y/n): ").lower() == "y"
symbols = input("Include symbols? (y/n): ").lower() == "y"

password = generate_password(length, letters, numbers, symbols)

if password:
    print("\nGenerated Password:")
    print(password)
else:
    print("Please select at least one character type.")