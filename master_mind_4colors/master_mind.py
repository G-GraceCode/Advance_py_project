import random

COLORS = ["R", "Y", "B", "W", "O", "P"]
CODE_LENGTH = 4
TRIES = 10


def generate_code():
    code = []
    for _ in range(CODE_LENGTH):
        color = random.choice(COLORS)
        code.append(color)
    return code


def guess_code():
    while True:
        guess = input("Guess code (4 color code letter): ").upper().split(" ")

        if len(guess) != CODE_LENGTH:
            print(f"Invalide Code, Please enter color of {CODE_LENGTH}.")
            continue

        for color in guess:
            if color not in COLORS:
                print(f"Color code {color} not fount in {COLORS}")
                break
        else:
            break

    return guess


def check_code(guess, real_code):
    color_counts = {}
    correct_posi = 0
    incorrect_posi = 0

    # Checking each of color code are there in random code & storing in a dic

    for color in real_code:
        # in dic, check the keys in the dic, if a code is present or not
        if color not in color_counts:
            color_counts[color] = 0
        color_counts[color] += 1

    """ zip take two items from diff list at same position to for a turple in a list 
        g = [1, 3]
        r = [1, 3]
        zip = [(1, 1), (3, 3)]
        """

    # Colors in the correct position
    for guess_color, real_color in zip(guess, real_code):
        if guess_color == real_color:
            correct_posi += 1
            color_counts[guess_color] -= 1

    # Colors for incorrect_posi
    for guess_color, real_color in zip(guess, real_code):
        if guess_color in color_counts and color_counts[guess_color] > 0:
            incorrect_posi += 1
            color_counts[guess_color] -= 1

    return correct_posi, incorrect_posi


def game():

    print("Welcome to the Mastermind Color Code Game...")
    print("The Color code are:", *COLORS)
    print(f"You have {TRIES} to find the code...")

    code = generate_code()

    for attempts in range(1, TRIES + 1):
        guess = guess_code()
        correct_posi, incorrect_posi = check_code(guess, code)

        if (correct_posi == CODE_LENGTH):
            print(f"You guess the code in {attempts} tries")
            break
        print(
            f"Correct Positions: {correct_posi} | Incorrect Position: {incorrect_posi}")

    else:
        print("You ran out of Tries, the code Was", *code)


if __name__ == "__main__":
    game()
