"""EX02 - Chardle - A cute step toward Wordle."""

__author__ = "730741801"

def input_word() -> str:
    """Prompt the user to enter a 5-character word."""
    word = input("Enter a 5-character word: ")
    if len(word) != 5:
        print("Error: Word must contain 5 characters.")
        exit()
    return word

def input_letter() -> str:
    """Prompt the user to enter a single character."""
    letter: str = input("Enter a single character: ")
    if len(letter) != 1:
        print ("Error: Character must be a single character.")
        exit()
    return letter

def contains_char(word: str, letter: str) -> None:
    """Check each index of the word to see if it matches the character."""
    print(f"Searching for {letter} in {word}")
    count: int = 0
    if word[0] == letter:
        print(f"{letter} found at index 0")
        count += 1
    if word[1] == letter:
        print(f"{letter} found at index 1")
        count += 1
    if word[2] == letter:
        print(f"{letter} found at index 2")
        count += 1
    if word[3] == letter:
        print(f"{letter} found at index 3")
        count += 1
    if word[4] == letter:
        print(f"{letter} found at index 4")
        count += 1
    if count == 0:
        print(f"No instances of {letter} found in {word}")
    else:
        if count == 1:
            print(f"1 instance of {letter} found in {word}")
        else:
            print(f"{count} instances of {letter} found in {word}")

def main() -> None:
    """Starts the program and calls the functions."""
    contains_char(word=input_word(), letter=input_letter())


if __name__ == "__main__":
    main()