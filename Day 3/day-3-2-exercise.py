# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
brut_bmi = weight / (height ** 2)
bmi = round(brut_bmi)

if bmi < 18.5:
	print(f"Your BMI score is {bmi}, you're underweight.")
elif bmi < 25:
	print(f"Your BMI score is {bmi}, you have a normal weight")
elif bmi < 30:
	print(f"Your BMI score is {bmi}, you're slightly overweight.")
elif bmi < 35:
	print(f"Your BMI score is {bmi}, you're obese.")
else:
	print(f"Your BMI score is {bmi}, you're clinically obese.")
