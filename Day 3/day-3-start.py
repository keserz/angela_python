print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height >= 120:
	print("You can ride the roller coaster!")
	age = int(input("How old are you ?"))
	if age < 12:
		print("It will cost $5")
	elif age > 18:
		print("It will cost $12")
	else:
		print("It will cost $7")
else:
	print("Sorry, you can't ride the roller coaster :(.")
