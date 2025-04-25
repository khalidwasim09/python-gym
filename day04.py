import random 
def get_computer_choice(): 
    choices = ["rock", "paper", "scissors"]
    return random.choice(choices)

users_choice = input("Enter your choice: ").lower() 
print(f"User's Choice: {users_choice}")
computers_choice = get_computer_choice()
print(f"Computer's Choice: {computers_choice}")

if users_choice == computers_choice:
    print("DRAW") 
    
elif users_choice == "rock": 
    if computers_choice == "scissors": 
        print("You win! Rock cruhses scissors")
    else: 
        print("You lose! Paper covers rock")
        
elif users_choice == "paper": 
    if computers_choice == "rock": 
        print("You win! Paper covers rock") 
    else: 
        print("You lose! Scissors cut paper") 

elif users_choice == "scissors": 
    if computers_choice == "rock": 
        print("You lose! Rock breaks scissors")
    else: 
        print("You win! Scissors cut paper")

else:
    print("Invalid input. Please enter rock, paper, or scissors.")

        
        