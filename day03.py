def calculate_bmi(height_cm, weight_kg):
    height_m = height_cm / 100
    bmi = weight_kg / (height_m **2)
    return bmi 
user_weight = int(input("Enter your weight in kg: "))
user_height = int(input("Enter your height in cm: "))

bmi = calculate_bmi(user_height, user_weight)

print(f"Your bmi is {bmi:.1f}")
if bmi < 18: 
    print ("You are underweight")
elif bmi < 25: 
    print("You are normal")
elif bmi < 30: 
    print("You are overweight")
else: 
    print("You are obese")

# Tip calculator 

def calculate_total(bill_amount, tip_percentage): 
    tip_decimal = tip_percentage / 100 
    total = bill_amount + (tip_decimal * bill_amount)
    return total 
bill = int(input("Enter bill amount: "))
tip  = int(input("Enter tip percentage: ")) 

final_amount = calculate_total(bill, tip)
print(f"Your total bill including tip is {final_amount:.2f}")

    