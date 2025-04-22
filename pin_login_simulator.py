correct_pin = "1234" 
attempts_left = 3

while attempts_left > 0: 
    user_input = input("Enter your pin: ")
    if user_input == correct_pin:
        print("Access granted ")
        break 
    else: 
        attempts_left -= 1
    if attempts_left > 0: 
        print(f"Wrong {attempts_left} attempts left ") 
        
    
    else: 
        print("Account Locked Too many wrong attempt ")
        