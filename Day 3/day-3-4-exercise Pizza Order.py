# 🚨 Don't change the code below 👇
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
while size != "S" and size != "M" and size != "L":
	size = input("I didn't understand the size of your pizza, write : S, M or L  in caps please.")

add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
# 🚨 Don't change the code above 👆

# W rite your code below this line 👇

if size == "S":
	price = 15
elif size == "M":
	price = 20
elif size == "L":
	price = 25

if add_pepperoni == "Y" and size == "S":
	price += 2
elif add_pepperoni == "Y" and size == "M" or size == "L":
	price += 3

if extra_cheese == "Y":
	price += 1

print(f"Your final bill is ${price}")
