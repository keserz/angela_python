# HINT: You can call clear() to clear the output in the console.

import art

print(art.logo)

print("Welcome to the secret auction, other biders can't see your bid !")

auction = {}
no_bider_left = False

while no_bider_left == False:
	name = input("What is your name ? ")
	bid = int(input("What is your bid ? $"))
	auction[name] = bid
	end_cond = input("Is there any more bider left ? type 'Yes' or 'No'").lower()
	if end_cond == 'no':
		no_bider_left = True

bider = ""
highest_bid = 0
for bid in auction:
	print(bid)
	if auction[bid] > highest_bid:
		highest_bid = auction[bid]
		bider = bid

print(f"Congratulation {bider}, you won the auction with a bid of ${highest_bid}")

