#!/usr/bin/python3

balance = 3000
daily_limit = 500

def get_requested():
	while True:
		print("Please enter the money to withdraw: ", end="")
		try:
			requested = int(input())
		except ValueError:
			print("Invalid input!")
		if requested < 0:
			print("You have to have a positive number!")
		else:
			return requested

while True:
	requested = get_requested()
	if requested > daily_limit:
		print("You fail at budgeting - your daily limit is exceeded!")
		continue
	if requested > balance:
		print("You fail at budgeting - your balance is exceeded!")
		continue
	if balance < 100:
		charge = requested * 0.025
		print("You are being charged " + str(charge) + " because your balance is low!")
	else:
		charge = 0
	print("Withdrawal successful!")
	balance -= (requested + charge)
	daily_limit -= requested
