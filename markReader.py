#!/usr/bin/python

def main():
	# Schedule the marks and see what happens.
	for i in range(10):
		while not getMark():
			continue

def getMark():
	# Take a mark from stdin and process it.
	# Returns false upon failure and true upon success.
	print("Please enter your mark: ")
	mark = raw_input()
	# Check for errors.
	try:
		int(mark)
	except:
		print("You need to enter a number!")
		return False
	if int(mark) > 100 or int(mark) < 0:
		print("Mark is out of range! Please try again.")
		return False
	else:
		if int(mark) < 39:
			print("You failed with " + mark + "%.")
			return True
		elif int(mark) < 59:
			print("You passed with " + mark + "%.")
			return True
		else:
			print("You got a distinction with " + mark + "%.")
			return True

main()
