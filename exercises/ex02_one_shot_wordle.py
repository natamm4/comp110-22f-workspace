"""EX02 - One-Shot Worldle - Loops!"""

__author__ = "730557757"


secret: str = "python"
guess: str = input(f"What is your {int(len(secret))}-letter guess? ")
where: int = 0
emoji: str = ""
WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"

while len(guess) != int(len(secret)):
    guess = input("That was not 6 letters! Try again: ")
while where < len(secret):
    if guess[where] == secret[where]:
        emoji += GREEN_BOX
    else:
        exists: bool = False
        matches: int = 0
        while (exists is not True) and (matches < len(secret)):
            if guess[where] == secret[matches]:
                exists = True
            else:
                matches += 1  
        if exists is True:
            emoji += YELLOW_BOX
            exists = False
        else: 
            emoji += WHITE_BOX
    where += 1
print(emoji)

if len(guess) == int(len(secret)):
    if guess == secret:
        print("Woo! You got it!")
    else:
        print("Not quite. Play again soon!")