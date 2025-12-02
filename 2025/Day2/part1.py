with open("input.txt", mode="r") as file:
	lines = file.readlines()

def isInvalidId(number):
	s = str(number)
	length = len(s)
	if (length % 2 == 1):
		return False
	mid = length // 2
	first_half = int(s[:mid])
	second_half = int(s[mid:])
	if first_half == second_half:
		print(number, ' is twice ', first_half, second_half)
		return True
	return False

sum = 0

for line in lines:
	ids = line[:(len(line))].split(',')
	print(ids)
	for id in ids:
		Ranges = id.split('-')
		for i in range(int(Ranges[0]), int(Ranges[1]) + 1):
			if (isInvalidId(i)):
				sum += i

print(sum)
