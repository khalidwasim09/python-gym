import random 
secret_number = random.randint(1,1000000)
attempts = 0 

while True: 
    try: 
        user_input = int (input("Guess the number (1-100): "))
        attempts += 1 
        
        if user_input < 1 or user_input > 1000000: 
            print("Please guess a number between 1 and 100")
        elif user_input < secret_number: 
            print("Too low")
        elif user_input > secret_number: 
            print("Too high") 
        else: 
            print(f"Congratulations! You guesssed it in {attempts} tries")
    except ValueError: 
        print("Invalid input! Please enter a number")
        