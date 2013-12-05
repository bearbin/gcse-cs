#!/usr/bin/python

import sys

sum = 0

while True:
	userI = raw_input()
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
