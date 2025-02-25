import random

def generate_number(diff):
    return random.randint(1, diff)

def get_guess_from_user(user_diff):
    while True:
        try:
            guess = int(input(f"Guess a number between 1 to {user_diff}: "))
            if guess > user_diff:
                print("Please enter a valid guess.")
            else:
                return guess
        except ValueError:
            print("Please enter a valid number.")

def compare_results(secret_number, user_guess):
    if secret_number == user_guess:
        return True
    else:
        return False

def play(diff):
    secret_number = generate_number(diff)
    user_guess = get_guess_from_user(diff)
    result = compare_results(secret_number, user_guess)
    if result:
        print("Bingo!")
    else:
        print(f"Incorrect, the number was {secret_number}. Better luck next time!")