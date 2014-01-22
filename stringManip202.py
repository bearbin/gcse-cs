#!/usr/bin/python3

import sys

print("Please input a string for processing:")
stringInput = input()
stringLength = len(stringInput)
print("Length: " + str(stringLength))
print("First Four: " + stringInput[:4])
print("Last Four: " + stringInput[-4:])
print("What is your start index?")
while True:
	startIndex = input()
	try:
		startIndex = int(startIndex)
	except ValueError:
		print("Please enter a valid index!")
		continue
	else:
		if startIndex > stringLength or startIndex < 0:
			print("Please enter a valid index!")
			continue
		else:
			break
while True:
	endIndex = input()
	try:
		endIndex = int(endIndex)
	except ValueError:
		print("Please enter a valid index!")
		continue
	else:
		if endIndex > stringLength or endIndex < 0:
			print("Please enter a valid index!")
			continue
		else:
			break
print(stringInput[startIndex:endIndex])
