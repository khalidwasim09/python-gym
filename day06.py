import random 
random_integer = random.randint( 1, 100)
while True: 
    user_input = input("Guess the number") 
    if user_input == random_integer: 
        print("Congratulations")
    if user_input < 1: 
        print("Too low! Choose between 1 and 100")
    if user_input > 100: 
        print("Too high! Choose between 1 and 100")