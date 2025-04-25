import random

def get_computer_choice():
    choices = ["rock", "paper", "scissors"]
    return random.choice(choices)

# Score counters
wins = 0
losses = 0
draws = 0

while True:
    users_choice = input("Enter your choice (rock, paper, scissors): ").lower()
    print(f"User's choice: {users_choice}")

    computers_choice = get_computer_choice()
    print(f"Computer's choice: {computers_choice}")

    if users_choice == computers_choice:
        print("It's a draw")
        draws += 1
    elif users_choice == "rock":
        if computers_choice == "scissors":
            print("You win! Rock breaks scissors")
            wins += 1
        elif computers_choice == "paper":
            print("You lose! Paper wraps rock")
            losses += 1
        else:
            print("Invalid input! Please choose rock, paper or scissors")
    elif users_choice == "scissors":
        if computers_choice == "rock":
            print("You lose! Rock breaks scissors")
            losses += 1
        elif computers_choice == "paper":
            print("You win! Scissors cut paper")
            wins += 1
        else:
            print("Invalid input! Please choose rock, paper or scissors")
    elif users_choice == "paper":
        if computers_choice == "scissors":
            print("You lose! Scissors cut paper")
            losses += 1
        elif computers_choice == "rock":
            print("You win! Paper wraps rock")
            wins += 1
        else:
            print("Invalid input! Please choose rock, paper or scissors")
    else:
        print("Invalid input! Please choose rock, paper or scissors")
        continue  # Don’t ask to play again, just retry the round

    # Ask if the user wants to play again
    play_again = input("Play again? (yes/no): ").lower()
    if play_again != "yes":
        break

# Print the final scores
print("\nFinal Scores:")
print(f"Wins:   {wins}")
print(f"Losses: {losses}")
print(f"Draws:  {draws}")
print("Thanks for playing!")
