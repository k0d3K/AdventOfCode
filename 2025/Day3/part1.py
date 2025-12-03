with open("input.txt", mode="r") as file:
	lines = file.readlines()

sum = 0

for line in lines:
	numbers = [int(x) for x in line.strip()]
	max = 0
	for i in range(0, len(numbers)):
		for j in numbers[i+1:]:
			number = int(numbers[i]) * 10 + int (j)
			if number > max:
				max = number
	print(max)
	sum += max

print(sum)
