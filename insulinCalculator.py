# Create a variable asking the user what ratio they are on. 
# 1 unit per a specific amount of carbs
scale = int(input("What Carb/insulin ratio are you on? Type the number of carbs per one unit. "))

# Create another variable asking user the amount of carbs they are going to eat with their meal. 
ratio = int(input("How many carbs is your meal/snack? "))

# This last variable will be the amount of carbs user will eat divided ÷ by the number of cards per 1
# unit the user is on for the amount of insulin 
units_of_insulin = ratio / scale

print(f"You need to take {units_of_insulin} units of insulin. Enjoy your meal.")
