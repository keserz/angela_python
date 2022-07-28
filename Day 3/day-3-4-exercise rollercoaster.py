print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm ? "))

if height >= 120:
	print("You can ride the roller coaster!")
	age = int(input("How old are you ? "))
	if age < 12:
		price = 5
	if age > 18:
		price = 12
	else:
		price = 7

	photo = input("Would you like to take a picture for $3 ? yes/no. ")
	if photo == "yes":
		price += 3

	print(f"the total of the ride is ${price}.")

else:
	print("Sorry, you can't ride the roller coaster :(.")
