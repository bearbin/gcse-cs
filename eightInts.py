#!/usr/bin/python

import sys

derp = []

for i in range(8):
	while True:
		x = raw_input()
		try:
			derp.append(int(x))
		except:
			print(e)
			sys.stderr.write("Non-integer entered!\n")
			continue
		else:
			break
		
derp.sort()

print(derp[0])
print(derp[7])
