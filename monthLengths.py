#!/usr/bin/python3

import calendar
from datetime import date

months = { 
	"january": "31",
	"february": "29" if calendar.isleap(date.today().year) else "28",
	"march": "31",
	"april": "30",
	"may": "31",
	"june": "30",
	"july": "31",
	"august": "31",
	"september": "30",
	"october": "31",
	"november": "30",
	"december": "31"
}

while True:
	print("Please choose a month (use it's name, not number): ")
	userInput = input()
	if months[userInput.lower()] == None:
		print("Invalid Month!")
		continue
	print(userInput + " has " + months[userInput.lower()] + " days.")
