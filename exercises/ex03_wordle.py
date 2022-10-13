"""EX03 - Structured Wordle."""

__author__ = "730557757"


def contains_char(multiple_char: str, single_char: str) -> bool:
    """Returns True or False based on whether the single character is found within the longer string or not."""
    assert len(single_char) == 1
    where_char: int = 0
    while where_char < len(multiple_char):
        if single_char == multiple_char[where_char]:
            return True
        else:
            where_char += 1  
    else:
        return False


def emojified(guess: str, secret: str) -> str:
    """Return a string of emojis showing whether the characters in a guess match those in the secret."""
    assert len(guess) == len(secret)
    index: int = 0
    emoji: str = ""
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"
    while index < len(secret):
        if guess[index] == secret[index]:
            emoji += GREEN_BOX
        else:
            if contains_char(secret, guess[index]) is True:
                emoji += YELLOW_BOX
            else: 
                emoji += WHITE_BOX
        index += 1
    return emoji


def input_guess(expected_len: int) -> str:
    """Makes user reenter word if not the right amount of letters."""
    guess: str = input(f"Enter a {int(expected_len)} character word: ")
    while len(guess) != expected_len:
        guess = input(f"That wasn't {int(expected_len)} chars! Try again: ")
    return guess


def main() -> None:
    """The entrypoint of the program of main game loop."""
    secret: str = "codes"
    guess: str = ""
    turns: int = 1
    win: bool = False
    while (win is False) and (turns <= 6):
        print(f"=== Turn {turns}/6 ===")
        guess = input_guess(len(secret))
        print(emojified(guess, secret)) 
        if guess == secret:
            win = True
        else:
            turns += 1
    if win is True:
        print(f"You won in {turns}/6 turns!")
    else: 
        print("X/6 - Sorry, try again tomorrow!")
    

if __name__ == "__main__":
    main()