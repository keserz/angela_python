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


def calculator(number1, number2):
	return operation[operation_symbol](number1, number2)


operation = {"+": add,
             "-": sub,
             "*": multiple,
             "/": divide,
             }

exit_calc = False

num1 = int(input("What's the first number ?: "))

"""Print only the key in a dictionary"""
for key in operation:
	print(key)

operation_symbol = input("Pick an operation from the lines above: ")
num2 = int(input("What's the second number ?: "))

answer = calculator(num1, num2)
print(type(answer))
print(f"{num1} {operation_symbol} {num2} = {answer}")
while not exit_calc:
	num1 = answer
	continue_calc = input(f"type 'y' to continue calculating with {answer}, or type 'n' to exit.")
	if continue_calc == 'n':
		exit_calc = True
	operation_symbol = input("Pick another operation: ")
	num2 = int(input("What's the next number ?: "))

	answer_next = calculator(answer, num2)
	print(f"{answer} {operation_symbol} {num2} = {answer_next}")
	answer = answer_next
