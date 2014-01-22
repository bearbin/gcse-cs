#!/usr/bin/python3

values = {"bun": 50, "coffee": 120, "cake": 150, "sandwich": 210, "dessert": 400}
takings = {"bun": 0, "coffee": 0, "cake": 0, "sandwich": 0, "dessert": 0}
 

while "the universe is working":
	itemSold = input().lower()
	if itemSold == "end":
		totalTakings = sum(takings.values())
		print("Total takings: $" + str(totalTakings // 100) + "." + str(totalTakings % 100))
		inverseTakings = {v: k for k, v in takings.items()}
		biggestItem = inverseTakings[max(takings.values())]
		biggestItemUnits = takings[biggestItem] // values[biggestItem]
		print("Highest: " + biggestItem + " (" + str(biggestItemUnits) + " unit" + (")" if biggestItemUnits == 1 else "s)"))
		break
	else:
		try:
			takings[itemSold] += values[itemSold]
		except KeyError:
			print("Bad input!")
	
