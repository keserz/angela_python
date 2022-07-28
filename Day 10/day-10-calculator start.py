import art

print(art.logo)


# Calculator

def add(n1, n2):
	return n1 + n2


def sub(n1, n2):
	return n1 - n2


def multiple(n1, n2):
	return n1 * n2


def divide(n1, n2):
	return n1 / n2


operation = {"+": add,
             "-": sub,
             "*": multiple,
             "/": divide,
             }

num1 = int(input("What's the first number ?: "))

"""Print only the key in a dictionary"""
for key in operation:
	print(key)

operation_symbol = input("Pick an operation from the lines above: ")
num2 = int(input("What's the second number ?: "))


def calculator(number1, number2):
	return operation[operation_symbol](number1, number2)


first_answer = calculator(num1, num2)
print(type(first_answer))
print(f"{num1} {operation_symbol} {num2} = {first_answer}")

operation_symbol = input("Pick another operation: ")
num3 = int(input("What's the third number ?: "))

second_answer = calculator(first_answer, num3)

print(f"{first_answer} {operation_symbol} {num3} = {second_answer}")
