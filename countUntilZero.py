#!/usr/bin/python3

import sys

sum = 0

while True:
	userI = input()
	try:
		userI = int(userI)
	except:
		sys.stderr.write("Non-integer entered!\n")
		break
	else:
		sum += userI
		if userI < 1:
			break

print(sum)
