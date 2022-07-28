# Nesting
capital = {
	"France": "Paris",
	"Germany": "Berlin",
}

# Nesting a list in a Dictionary

travel_log = {
	"France": ["Paris", "Lille", "Dijon"],
	"Germany": ["Berlin", "Hamburg", "Stuttgart"],
}

# Nesting a list in a list
["A", "B", ["C", "D"]]

# Nesting a Dictionary in a Dictionary

travel_log = {
	"France": {"cities_visited": ["Paris", "Lille", "Dijon"], "total_visits": 12},
	"Germany": {"cities_visited": ["Berlin", "Hamburg", "Stuttgart"], "total_visits": 5},
}

# Nesting a Dictionary in a list

travel_log = [
	{
		"country": "France",
		"cities_visited": ["Paris", "Lille", "Dijon"],
		"total_visits": 12},
	{
		"country": "Germany",
		"cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
		"total_visits": 5},
]

# add +1 to every value
dict = {
    "a": 1,
    "b": 2,
    "c": 3,
}
for key in dict:
	dict[key] += 1
print(dict)


# print steak
order = {
    "starter": {1: "Salad", 2: "Soup"},
    "main": {1: ["Burger", "Fries"], 2: ["Steak"]},
    "dessert": {1: ["Ice Cream"], 2: []},
}
print(order["main"][2][0])