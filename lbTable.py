#!/usr/bin/python

conversionRatio = 0.453592

for i in range(20):
	print(str(i+1) + " lb - " + str( round( (i+1) * conversionRatio, 3) ) + " kg")
