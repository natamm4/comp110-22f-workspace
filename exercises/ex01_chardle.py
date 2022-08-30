"""EX01 - Chardle - A cute step toward Wordle."""

__author__ = "730557757"

user_word: str = input("Enter a 5-character word: ")
if len(user_word) == 5:
    user_character: str = input("Enter a single character: ")
    if len(user_character) == 1:
        print("Searching for " + user_character + " in " + user_word)

        if user_character in user_word:
            character_instances: int = 0
            if(user_character == user_word[0]):
                print(user_character + " found at index 0")
                character_instances = character_instances + 1
            if(user_character == user_word[1]):
                print(user_character + " found at index 1")
                character_instances = character_instances + 1
            if(user_character == user_word[2]):
                print(user_character + " found at index 2")
                character_instances = character_instances + 1
            if(user_character == user_word[3]):
                print(user_character + " found at index 3")
                character_instances = character_instances + 1
            if(user_character == user_word[4]):
                print(user_character + " found at index 4")
                character_instances = character_instances + 1

            if(character_instances == 1):
                print(str(character_instances) + " instance of " + user_character + " found in " + user_word)
            else:
                print(str(character_instances) + " instances of " + user_character + " found in " + user_word)

        else:
            print("No instances of " + user_character + " found in " + user_word)

    else:
        print("Error: Character must be a single character.")

else:
    print("Error: Word must contain 5 characters")
    exit()