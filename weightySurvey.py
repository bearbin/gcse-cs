#!/usr/bin/python3

# Configuration
students_tested = 5 # Number of students to read the height/weight of, would be 1000 for the real thing.

weights = []
heights = []

def get_height():
	while 1:
		print("Height: (cm) ", end="")
		try:
			height = int(input())
		except ValueError:
			print("Invalid height!")
			continue
		if height > 220 or height < 20:
			print("Invalid height!")
			continue
		else:
			break
	return height

def get_weight():
	while 1:
		print("Weight: (kg) ", end="")
		try:
			weight = int(input())
		except ValueError:
			print("Invalid weight!")
			continue
		if weight > 160 or weight < 20:
			print("Invalid weight - that's a strange student!")
			continue
		else:
			break
	return weight

for i in range(students_tested):
	print("Student " + str(i+1))
	heights.append(get_height())
	weights.append(get_weight())

print("Average Height: " + str(sum(heights) / len(heights)))
print("Average Weight: " + str(sum(weights) / len(weights)))
