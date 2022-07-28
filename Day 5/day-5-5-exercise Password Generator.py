# Password Generator Project
import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# Eazy Level - Order not randomised:
# e.g. 4 letter, 2 symbol, 2 number = JduE&!91

first = ""
second = ""
third = ""
lfirst = []
lsecond = []
lthird = []

for n in range(0, nr_letters):
	test = random.randint(0, len(letters) - 1)
	# print(type(test))
	# print(type(first))
	# print(type(nr_letters[test]))
	first = first + letters[test]
	lfirstn = [letters[test]]
	lfirst = lfirst + lfirstn
for n in range(0, nr_symbols):
	test = random.randint(0, len(symbols) - 1)
	second = second + symbols[test]
	lsecondn = [symbols[test]]
	lsecond = lsecond + lsecondn

for n in range(0, nr_numbers):
	test = random.randint(0, len(numbers) - 1)
	third = third + numbers[test]
	lthirdn = [numbers[test]]
	lthird = lthird + lthirdn
password = first + second + third
print("Password : " + password)


random_list = lfirst + lsecond + lthird


random.shuffle(random_list)

final_password = ""
for n in range(len(random_list)):
	final_password = final_password + random_list[n]
print("Random password : " + final_password)


# Hard Level - Order of characters randomised:
# e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
