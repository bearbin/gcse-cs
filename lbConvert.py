#!/usr/bin/python

import sys

conversionRatio = 0.453592

while True:
	userInput = raw_input()
	try:
		int(userInput)
	except:
		sys.stderr.write("Non-integer entered!\n")
		continue
	else:
		print( userInput + " lb = " + str(round(int(userInput) * conversionRatio, 3)) + " kg" )
