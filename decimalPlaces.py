#!/usr/bin/python3

number = input()
print(round(float(number)))
dotloc = number.find(".")
if dotloc != -1:
	print(number[:dotloc])
else:
	print(number)
