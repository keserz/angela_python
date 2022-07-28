import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# Write your code below this line 👇
player = input("Welcome to the most amazing Rock Paper Scissors on the planet, what's your next move ? type '1' for "
               "rock, '2' for paper or '3' for scissors.")
player = int(player)

while player != 1 and player != 2 and player != 3:
	player = input("I did not catch your next move. what's your next move ? type '1' for rock, '2' for paper or '3' "
	               "for scissors.")
	player = int(player)

computer = random.randint(1, 3)

one = rock
two = paper
three = scissors

if player == 1:
	if computer == 1:
		print(f"{one} vs {one}, it's a draw, nobody wins")
	elif computer == 2:
		print(f"{one} vs {two}, computer wins ! Try again")
	else:
		print(f"{one} vs {three}, you win ! Congrats")

if player == 2:
	if computer == 1:
		print(f"{two} vs {one}, you win ! Congrats")
	elif computer == 2:
		print(f"{two} vs {two}, it's a draw, nobody wins")
	else:
		print(f"{two} vs {three}, computer wins ! Try again")

if player == 3:
	if computer == 1:
		print(f"{three} vs {one}, computer wins ! Try again")
	elif computer == 2:
		print(f"{three} vs {two}, you win ! Congrats")
	else:
		print(f"{three} vs {three}, it's a draw, nobody wins")
