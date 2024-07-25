import random
import time


def extra_lines(lines):
    """Print extra lines to clear the screen."""
    for _ in range(lines):
        print()


def gen_sequence(lengths):
    """Generate a random sequence of numbers."""
    ran_sequence = [random.randint(1, 99) for _ in range(lengths)]
    return ran_sequence


def display(flow, difficulty):
    """Display the sequence with appropriate time delay"""
    print("Memorize the following sequence:")
    print(flow)
    if difficulty == "easy":
        time.sleep(5)  # Adjust the sleep duration for easy difficulty
    elif difficulty == "hard":
        time.sleep(7)  # Adjust the sleep duration for hard difficulty
    extra_lines(30)


def set_difficulty(difficulty):
    """Set difficulty level and return sequence length."""
    if difficulty == "easy":
        return 5
    elif difficulty == "hard":
        return 10
    else:
        print("Enter a valid level")


def user_input(seq_length):
    """Asks the user to input the numbers in no particular order."""
    print("Now, input the numbers in any order:")
    user_guess = []
    for _ in range(seq_length):
        guess = int(input(f"Enter number and press enter:"))
        user_guess.append(guess)
    return user_guess


def calc_score(sequence, user_guess):
    """Calculate score based on correct guessed numbers and returns the score."""
    user_score = 0
    for num in user_guess:
        if num in sequence:
            user_score += 1
    return user_score


game_on = True
while game_on:
    print("Exercise your mind and sharpen your memory in our memory game! 😁😁")
    level = input("Pick a difficulty (easy or hard): ").lower()
    length = set_difficulty(difficulty=level)
    order = gen_sequence(length)
    display(order, difficulty=level)
    user_input_sequence = user_input(length)
    score = calc_score(order, user_input_sequence)

    print("The sequence:", order)
    print("Your input sequence:", user_input_sequence)
    print("Your score:", score, "out of", length)

    if score == length:
        print("Omo, your brain sharp!")
    elif score == 0:
        print("Omo, you need help!")
    else:
        print("You dey try small small")

    end_of_game = input("Do you want to continue? Type 'yes' to continue or 'no' to end: ").lower()
    if end_of_game == "no":
        game_on = False
