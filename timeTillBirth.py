#!/usr/bin/python3

import datetime

months = {"jan":1, "feb":2, "mar":3, "apr":4, "may":5, "jun":6, "jul":7, "aug":8, "sep":9, "oct":10, "nov":11, "dec":12}

print("Please enter your birthday (05 jan format): ")
birthday = input()

nextBirthday = datetime.datetime(datetime.date.today().year + 1, months[birthday[3:]], int(birthday[:2])) - datetime.datetime.now()

print(nextBirthday.days)
