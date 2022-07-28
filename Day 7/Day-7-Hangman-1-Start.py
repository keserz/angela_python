# Step 1
import random
import os

def clear():
	os.system('cls')

word_list = ["aardvark", "baboon", "camel"]

# TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.

chosen_word = random.choice(word_list)

# TODO-1.1 : Create an empty List called display. For each letter in the chosen_word, add a "_" to 'display'. So if
#  the chosen_word was "apple", display should be ["_", "_", "_", "_", "_"] with 5 "_" representing each letter to
#  guess.

list_chosen_word = []
for i in chosen_word:
	list_chosen_word = list_chosen_word + list("_")

looser = 5
end_game = False
print(f"Pssst. The solution is {chosen_word}.")

# TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.


# TODO-2.2: - Loop through each position in the chosen_word; If the letter at that position matches 'guess' then reveal
#  that letter in the display at that position. e.g. If the user guessed "p" and the chosen word was "apple",
#  then display should be ["_", "p", "p", "_", "_"].
while not end_game:
	clear()
	print("")
	print(f"{' '.join(list_chosen_word)}")
	user_guess = input("Chose a letter : ").lower()
	if len(user_guess) > 1 or len(user_guess) < 1:
		user_guess = input("Please chose strictly 1 letter : ").lower()

	while list_chosen_word.count(user_guess) > 0:
		user_guess = input(f"You already chose the letter '{user_guess}', please chose another one : ").lower()
	count = chosen_word.count(user_guess)

	if count > 0:
		for i in range(len(chosen_word)):
			if user_guess == chosen_word[i] and user_guess != list_chosen_word[i]:
				list_chosen_word[i] = user_guess
		print(f"Good job ! you guessed a correct letter, now find the remaining letters")

	if count == 0:
		looser -= 1
		print(f"The letter {user_guess} isn't in the word, you lost a life, {looser} lives remaining")
		if looser == 0:
			print(f"Sorry you have {looser} live remaining, try again with another word")
			end_game = True

	if "_" not in list_chosen_word:
		print(f"Congratulation, you guessed the word {chosen_word}")
		end_game = True

# TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.


# TODO-3.1: - Print 'display' and you should see the guessed letter in the correct position and every other letter
#  replace with "_". Hint - Don't worry about getting the user to guess the next letter. We'll tackle that in step 3.
