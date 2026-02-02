import random

def generate_mad_lib(adjective, noun, verb):
    """
    Generates a short story using the provided words.

    This function demonstrates string formatting and function design
    by creating a Mad Libs-style story from user-provided words.

    Parameters
    ----------
    adjective : str
        An adjective to use in the story (e.g., "silly", "brave", "colorful").
    noun : str
        A noun to use in the story (e.g., "cat", "computer", "adventure").
    verb : str
        A past-tense verb to use in the story (e.g., "jumped", "crashed", "danced").

    Returns
    -------
    str
        A formatted story string that incorporates all three input words.
    """
    return f"On a {adjective} afternoon, a {noun} suddenly {verb} through the park, surprising everyone nearby."

def guessing_game():
    """
    Plays a number guessing game with the user.
    """
    secret_number = random.randint(1, 100)
    attempts = 0

    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")

    while True:
        guess = int(input("Enter your guess: "))
        attempts += 1

        if guess > secret_number:
            print("Too high! Try again.")
        elif guess < secret_number:
            print("Too low! Try again.")
        else:
            print(f"Congratulations! You guessed it in {attempts} attempts!")
            break

if __name__ == '__main__':
    guessing_game()
# dummy change to trigger workflow
# dummy change to trigger workflow
# trigger workflow
