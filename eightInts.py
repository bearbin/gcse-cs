#!/usr/bin/python3

import sys

derp = []

for i in range(8):
	while True:
		x = input()
		try:
			derp.append(int(x))
		except:
			sys.stderr.write("Non-integer entered!\n")
			continue
		else:
			break
		
derp.sort()

print(derp[0])
print(derp[7])
