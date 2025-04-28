scores = [] 
while True: 
    user_input = input("Enter a number or type 'done' to finish: ")
    if user_input == 'done': 
        break 
    try: 
        score = float(user_input) 
        scores.append(score)  
    except ValueError: 
        print("Invalid input, please enter a number or 'done'")
        
if scores: 
    print("\nHere are the results")
    print(f"The maximum number is {max(scores)}")
    print(f"The minimum score is {min(scores)}")
    print(f"The average score is {sum(scores) / len(scores):.2f}")  # .2f to round
else: 
    print("No scores were entered")