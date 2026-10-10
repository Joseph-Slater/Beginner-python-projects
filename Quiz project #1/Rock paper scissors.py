import random

user_wins = 0
computer_wins = 0
beats = {"rock": "scissors", "paper": "rock", "scissors": "paper"}

while True:
    user_choice = input("Choose rock, paper, scissors, or quit: ").lower().strip()
    if user_choice == "quit":
        break
    if user_choice not in ["rock", "paper", "scissors"]:
        print("Invalid choice. Please choose rock, paper, or scissors.")
        continue

    computer_choice = random.choice(["rock", "paper", "scissors"])
    print(f"Computer chose: {computer_choice}")
    if user_choice == computer_choice:
        print("It's a tie!")
    elif beats[user_choice] == computer_choice:
        print("You win this round!")
        user_wins += 1
    else:
        print("Computer wins this round!")
        computer_wins += 1

    print(f"Score - You: {user_wins}, Computer: {computer_wins}")
print(f"Final score - You: {user_wins}, Computer: {computer_wins}")
if user_wins > computer_wins:
    print("Congratulations! You won the game!")
elif user_wins < computer_wins:
    print("You lost! The computer won the game!")
else: 
    print("The game ended in a tie!")