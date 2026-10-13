import random
import time
from pathlib import Path

file_path = Path(__file__).parent / "highscore.txt"    #setting the file path

OPERATORS = ["+", "-", "*"]
MIN_OPERAND = 3
MAX_OPERAND = 12
TOTAL_PROBLEMS = 10


def generate_problem():
    left = random.randint(MIN_OPERAND, MAX_OPERAND)
    right = random.randint(MIN_OPERAND, MAX_OPERAND)
    operator = random.choice(OPERATORS)

    expr = str(left) + " " + operator + " " + str(right)
    answer = eval(expr)
    return expr, answer

while True:
# This is for the high score on start screen
    try:
        with open(file_path, "r") as f:
            best_time = float(f.read())
    except (FileNotFoundError, ValueError):
        best_time = None
    if best_time is None:
        print("Play to set a high score")
    else:
        print(f"Current high score: {best_time}")


    input("Press enter to start!")
    print("---------------------")

    start_time = time.time()
    correct = 0

# This is answering the question correctly or incorrectly
    for i in range(TOTAL_PROBLEMS):
        expr, answer = generate_problem()
        missed = False     # reset per question so we can count which questions are correct
        while True:
            guess = input(f"Problem #{i + 1}: {expr} = ? ")
            try:
                guess = int(guess)
            except ValueError:
                print("\033[31mPlease enter a valid number.\033[0m")
                continue
            if guess == answer:
                if not missed:
                    correct += 1
                break
            print("\033[1mIncorrect! Try again\033[0m")
            missed = True

# This is calculations for new highscore
    end_time = time.time()
    total_time = end_time - start_time
    if correct == TOTAL_PROBLEMS and (best_time is None or total_time < best_time):
        print("New high score!")
        with open(file_path, "w") as f:
            f.write(f"{total_time:.2f}")

# This is to see if they will play again
    print("---------------------")
    print(f"Nice work! You finished in {total_time:.2f} seconds.")
    print(f"You got {correct} out of {TOTAL_PROBLEMS} correct.")
    while True:
        play_again = input("Would you like to play again? (y/n) ").strip().lower()
        if play_again in ("y", "n"):
            break
        else:
            print("Invalid answer! Please type in y/n.")
            continue
    if play_again == "n":
        break
