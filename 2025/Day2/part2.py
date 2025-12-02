with open("input.txt", mode="r") as file:
	lines = file.readlines()

def isRepeated(s, digits):
	length = len(s)
	length_digits = len(digits)
	k = 0
	while k * length_digits < length:
		part = int(s[k * length_digits : (k + 1)* length_digits])
		if int(part) != int(digits):
			return False
		k += 1
	print(s, ' is ', k, ' times ', digits)
	return True

def isInvalidId(number):
	s = str(number)
	length = len(s)
	for i in range(1, length // 2 + 1):
		digits = s[:i]
		if isRepeated(s, digits):
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
