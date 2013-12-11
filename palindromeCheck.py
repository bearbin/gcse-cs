#!/usr/bin/python3

userInp = input()

if userInp == userInp[::-1]:
	print("Palindrome!")
else:
	print("That's not a palindrome :(")
