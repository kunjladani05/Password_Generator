import random
import string

from constants import PASSWORD_TOO_SHORT, ENTER_PASSWORD_LENGTH, GENERATED_PASSWORD


def generate_password(length):
    """
    Generate a secure password with at least one lowercase, one uppercase, one digit, and one special character.

    Parameters:
    length (int): The length of the password to be generated. Must be at least 6 characters.

    Returns:
    str: The generated password, or None if the length is less than 6.
    """
    if length < 6:
        print(PASSWORD_TOO_SHORT)
        return None

    # Define the character sets
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    digits = string.digits
    special = string.punctuation

    # Ensure the password has at least one of each type
    all_characters = lower + upper + digits + special
    password = [
        random.choice(lower),
        random.choice(upper),
        random.choice(digits),
        random.choice(special)
    ]

    # Fill the rest of the password length with random characters
    password += random.choices(all_characters, k=length - 4)

    # Shuffle the password list to avoid predictable patterns
    random.shuffle(password)

    return ''.join(password)


def main():
    """
    Main program that prompts the user for the desired password length and generates a secure password.
    """
    length = int(input(ENTER_PASSWORD_LENGTH))
    password = generate_password(length)
    if password:
        print(f"{GENERATED_PASSWORD}: {password}")


# Run the password generator
if __name__ == "__main__":
    main()
