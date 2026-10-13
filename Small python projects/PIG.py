import random

def roll():
    min_value = 1
    max_value = 6
    roll = random.randint(min_value, max_value)

    return roll

while True:
    players = input("How many players are playing? ")
    if players.isdigit():
        players = int(players)
        if 2 <= players <= 4:
            break   
        else:
            print("Please enter a number between 2 and 4.")
    else:
        print("Please enter a valid number.")

while True:
    max_score = input("What score should players reach to win? (recommended 20-100) ")
    if max_score.isdigit() and int(max_score) > 0:
        max_score = int(max_score)
        break
    else:
        print("Please enter a valid number.")

player_scores = [0 for _ in range(players)]

while max(player_scores) < max_score:

    for player_idx in range(players):
        current_score = 0
        print(f"\n\033[1;34mPlayer {player_idx + 1}'s turn.\033[0m\n")
        print(f"Your current score is {player_scores[player_idx]}.\n")
        while True:
            should_roll = input("Do you want to roll the dice? (yes/no) ").lower().strip()
            if should_roll not in ["y", "yes"]:
                break

            value = roll()
            if value == 1:
                print("\n\033[31mYou rolled a 1! You lose your turn.\033[0m")
                current_score = 0
                break

            print(f"\nYou rolled a {value}.")
            current_score += value
            print(f"Your score this turn is {current_score}\n")

            if player_scores[player_idx] + current_score >= max_score:
                print(f"\n\033[33mYou reached {player_scores[player_idx] + current_score} points! You win!\033[0m")
                break

        player_scores[player_idx] += current_score
        print(f"\033[32mYour total score is {player_scores[player_idx]}.\033[0m")
        if player_scores[player_idx] >= max_score:
            break


highest_score = max(player_scores)
winning_idx = player_scores.index(highest_score)
print(f"\n\033[1;33mPlayer number {winning_idx + 1} wins with a score of {highest_score}!\033[0m")
print("Final scores:")
for i, score in enumerate(player_scores):
    print(f"Player {i + 1}: {score}")