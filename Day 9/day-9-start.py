programming_dictionary = {
	"Bug": "An error in a program that prevents the program from running as expected.",
	"Function": "A piece of code that you can easily call over and over again.",
	"Loop": "The action of doing something over and over again",
}

# print(programming_dictionary["Bug"])

empty_dictionary = {}

# wipe an existing dictionary
# programming_dictionary = {}
# print(programming_dictionary)

# Edit an item in a dictionary
programming_dictionary["Bug"] = "A moth in your computer"
# print(programming_dictionary)

# loop through a dictionary
for thing in programming_dictionary:
	print(thing,":", programming_dictionary[thing])