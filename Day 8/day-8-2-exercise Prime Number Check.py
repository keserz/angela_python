# Write your code below this line 👇
def prime_checker(number):
	count = 0
	if number == 0 or number == 1:
		print(f"{number} is not a prime number")
	if number == 2:
		print(f"{number} is a prime number")
	for i in range(2, number-1):
		if number % i == 0:
			count += 1
	if count > 0:
		print(f"{number} is not a prime number")
	else:
		print(f"{number} is a prime number")


# Write your code above this line 👆

# Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number = n)


