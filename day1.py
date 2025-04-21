name = input("What's your name ? ")
age = int(input("What's your age ? "))

if age >= 18: 
    print (f"Welcome {name}! You're allowed in.") 
    city = input("What's your city ? ")
    
    if city.lower() == "toronto": 
        print("Welcome to the 6ix")
    else: 
        print(f"Nice to meet someone from {city}")

else: 
    print(f"Sorry {name}, you're too young")
