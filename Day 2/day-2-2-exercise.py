# 🚨 Don't change the code below 👇
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇

float_height = float(height)
int_weight = int(weight)

bmi = int_weight / (float_height ** 2)

print(round(bmi))

print(type(float_height), type(int_weight))

print(f"Your BMI is : {round(bmi)}.")
