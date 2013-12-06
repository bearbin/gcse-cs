#!/usr/bin/python3

import sys

alphabet = "abcdefghijklmnopqrstuvwxyz"
upper = 0

while True:
	start = input()[:1]
	if start.lower() in alphabet:
		break
	else:
		sys.stderr.write("Non-alphabet character entered.")
if start.isupper():
	upper += 1
start = alphabet.find(start.lower())

while True:
	stop = input()[:1]
	if stop.lower() in alphabet:
		break
	else:
		sys.stderr.write("Non-alphabet character entered.")
if stop.isupper():
	upper += 1
stop = alphabet.find(stop.lower())

if start > stop:
	tmp = stop
	stop = start
	start = tmp

if upper == 2:
	alphabet = alphabet.upper()

print(alphabet[start:stop+1])
