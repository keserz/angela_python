# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

total = name1.lower() + name2.lower()
tcount = total.count("t")
rcount = total.count("r")
ucount = total.count("u")
ecount = total.count("e")

lcount = total.count("l")
ocount = total.count("o")
vcount = total.count("v")
eecount = total.count("e")

true_count = tcount + rcount + ucount + ecount

love_count = lcount + ocount + vcount + eecount
result = str(true_count) + str(love_count)
result = int(result)

if result < 10 or result > 90:
	print(f"Your score is {result}, you go together like coke and mentos")
elif 40 <= result <= 50:
	print(f"Your score is {result}, you are alright together")
else:
	print(f"Your score is {result}")