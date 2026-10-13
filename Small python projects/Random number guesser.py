import random

top_of_range = input("Type the top of the range: ").strip()
if top_of_range.isdigit():
    top_of_range = int(top_of_range)
else:
    print("Please type a number next time.")
    quit()
if top_of_range <= 0:
    print("Please type a number larger than 0 next time.")
    quit()  

guesses = 0

while True:
    random_number = random.randint(0, top_of_range)
    if guesses == 0:
        user_guess = input("Make a guess: ")
    else:
        user_guess = input("Guess the new number: ")

    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print("Please type a number.")
        continue

    guesses += 1

    if user_guess == random_number:
        if guesses == 1:
            print(f"You got it in {guesses} guess!")
        else:
            print(f"You got it in {guesses} guesses!")
        break
    elif user_guess > random_number:
        guess_difference = user_guess - random_number
        print(f"You were {guess_difference} above the number!")
    else:
        guess_difference = random_number - user_guess
        print(f"You were {guess_difference} below the number!")
