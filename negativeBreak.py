#!/usr/bin/python

while True:
	userI = raw_input()
	try:
		lelo = int(userI)
	except:
		break
	else:
		if lelo < 0:
			break
