#!/usr/bin/python3

emailAddr = input()

atLoc = emailAddr.find("@")

if atLoc == -1:
	print(emailAddr)

print(emailAddr[:atLoc])
