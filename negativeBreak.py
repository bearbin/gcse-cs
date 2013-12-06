#!/usr/bin/python3

while True:
	userI = input()
	try:
		lelo = int(userI)
	except:
		break
	else:
		if lelo < 0:
			break
