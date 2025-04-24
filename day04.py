import random 
def get_computer_choice(): 
    choices = ["rock", "paper", "scissor"]
    return random.choice(choices)

users_choice = input("Enter your choice: ").lower() 
print(f"User's Choice: {users_choice}")
computers_choice = get_computer_choice()
print(f"Computer's Choice: {computers_choice}")

if users_choice == computers_choice:
    print("DRAW") 
    
    # Rock, Paper, Scissors game

# User's choice
user_choice = input("Choose rock, paper, or scissors: ").lower()

# Computer's choice
computer_choice = random.choice(["rock", "paper", "scissors"])

print(f"Computer chooses: {computer_choice}")

# Logic to determine the outcome
if user_choice == "rock":
    if computer_choice == "scissors":
        print("You win!")
    elif computer_choice == "paper":
        print("You lose!")
    else:
        print("It's a tie!")

elif user_choice == "paper":
    if computer_choice == "rock":
        print("You win!")
    elif computer_choice == "scissors":
        print("You lose!")
    else:
        print("It's a tie!")

elif user_choice == "scissors":
    if computer_choice == "paper":
        print("You win!")
    elif computer_choice == "rock":
        print("You lose!")
    else:
        print("It's a tie!")

else:
    print("Invalid choice!")
