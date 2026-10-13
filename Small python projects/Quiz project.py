print("Welcome to the geography quiz!")
play = input("Do you want to play? ")
attempts = 0
while True:
    if play.lower() != "yes":
        quit()
    else:
        print("Okay! Let's play :)")
        score = 0
        answer = input("What is the main colour of the Saudi Arabia flag? ")
        if answer.lower() == "green":
            print("Correct!")
            score += 1
        else:
            print("Incorrect! The correct answer is green.")

        answer = input("What continent is Seychelles in? ")
        if answer.lower().strip() == "africa":
            print("Correct!")
            score += 1
        else:
            print("Incorrect! The correct answer is Africa. ")

        answer = input("Which country is not a part of NATO: Turkey, France, or Ukraine?")
        if answer.lower().strip() == "ukraine":
            print("Correct!")
            score += 1
        else:
            print("Incorrect! The correct answer is Ukraine.")


        print(f"You got {score}/3 questions correct!")
        if score != 3:
            answer = input("Would you like to try again?")
            if answer.lower() == "yes":
                score = 0
                attempts += 1
            else: 
                print("Thanks for playing!")
                break
        else:
            print("Congratulations! You got all the questions correct!")
            break

quit()
