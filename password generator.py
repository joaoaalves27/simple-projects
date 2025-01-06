import random
import string

def generate_password():
    include_lowercase = input("Include lowercase letters (a-z)? (yes/no): ").lower()
    include_uppercase = input("Include uppercase letters (A-Z)? (yes/no): ").lower()
    include_digits = input("Include digits (0-9)? (yes/no): ").lower()
    include_symbols = input("Include symbols (e.g., !@#$%^&*)? (yes/no): ").lower()

    char_pool = ""

    if include_lowercase == "yes":
        char_pool += string.ascii_lowercase
    if include_uppercase == "yes":
        char_pool += string.ascii_uppercase
    if include_digits == "yes":
        char_pool += string.digits
    if include_symbols == "yes":
        char_pool += string.punctuation

    if not char_pool:
        print("You must select at least one character type (letters, digits, or symbols).")
        return

    length = int(input("Enter the desired password length: "))

    password = ''.join(random.choice(char_pool) for _ in range(length))

    print("\nGenerated password:", password)

generate_password()
