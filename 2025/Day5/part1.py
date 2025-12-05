with open("input.txt", mode="r") as file:
	lines = file.readlines()

def isInRange(thisRange, number):
	return number >= int(thisRange[0]) and number <= int(thisRange[1])

sum = 0
ranges = []
i = 0

while i < len(lines) + 1:
	if lines[i].strip() == "":
		break
	ranges.append(lines[i].strip().split('-'))
	i += 1

i += 1
while i < len(lines):
	number = int(lines[i].strip())
	for thisRange in ranges:
		print(thisRange, number)
		if isInRange(thisRange, number):
			sum += 1
			break
	i += 1

print(sum)
