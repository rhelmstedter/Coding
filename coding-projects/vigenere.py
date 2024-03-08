"""This module is a simple vigenere cipher."""

from string import ascii_uppercase
from itertools import cycle

LETTERS = ascii_uppercase


def main() -> None:
    """Handle the main logic of the vigenere cipher."""
    mode = get_mode()
    key = get_key()
    message = get_message(mode)
    translated_message = translate_message(mode, key, message)
    print_message(mode, translated_message)


def get_mode() -> str:
    """Get the mode from the user."""
    while True:
        print("Do you want to (e)ncrypt or (d)ecrypt?")
        response = input("> ").lower()
        if response.startswith("e"):
            mode = "encrypt"
            break
        elif response.startswith("d"):
            mode = "decrypt"
            break
        print("Please enter the letter e or d.")
    return mode


def get_key() -> str:
    """Get the key from the user."""
    while True:
        print("Please specify the key to use.")
        print("It can be a word or any combination of letters:")
        response = input("> ").upper()
        if response.isalpha():
            key = response
            break
    return key


def get_message(mode: str) -> str:
    """Get the message from the user."""
    print(f"Enter the message to {mode}.")
    message = input("> ").upper()
    return message


def translate_message(mode: str, key: str, message: str) -> str:
    """Encrypt or decrypt the message using the key."""
    translated = []
    key_char = cycle(key)
    for char in message:
        if char in LETTERS:
            idx = LETTERS.find(char)
            shift = LETTERS.find(next(key_char))
            if mode == "encrypt":
                new_idx = (idx + shift) % len(LETTERS)
            elif mode == "decrypt":
                new_idx = (idx - shift) % len(LETTERS)
            translated.append(LETTERS[new_idx])
        else:
            translated.append(char)
    return "".join(translated)


def print_message(mode: str, translated_message: str) -> None:
    """Print the mode and translated message."""
    print(f"{mode.title()}ed message:")
    print(translated_message)


if __name__ == "__main__":
    main()
