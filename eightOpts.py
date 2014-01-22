#!/usr/bin/python3

baseMoney = 53
options = ("Bacon", "Cheese Pie", "Orange", "Mashed Potato Roll", "Recooked Ham", "Baked Potato", "Salad Leaves", "Mouldy Bread")

def doOption(optionNumber):
	chosenOption = options[optionNumber - 1]
	print("You ordered " + chosenOption + " from BeribCo Industries Food Dept")
	cost = chosenOption.length() * 53
	print("Your " + chosenOption + " costs £" + str(cost // 100) + "." + str(cost % 100))
	pay(cost)

def pay(cost):
	while 1:
		print("Please insert payment (pence)")
		deduction = input()
		try:
			deduction = int(deduction)
		except ValueError:
			print("Please enter valid pence amount!")
			continue
		cost = cost - deduction
		if cost <= 0:
			return
		else:
			print("You have " + cost + "p left to pay!")
			continue


def main():
	while 1:
		j = 1
		for i in options:
			print(" (" + str(j) + ") " + i)
			j = j + 1
		print("Please choose an option: ")
		option = input()
		try:
			option = int(option)
		except ValueError:
			print("Please choose a valid option!")
			continue
		if option > 8 or option < 1:
			print("Please choose a valid option!")
			continue
		else:
			doOption(option)

main()
