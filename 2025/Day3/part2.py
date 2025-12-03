with open("input.txt", mode="r") as file:
	lines = file.readlines()

sum = 0

for line in lines:
	numbers = [int(x) for x in line.strip()]
	result = []
	start = 0
	for _ in range(12):
		best_digit = -1
		best_pos = start
		for i in range(start, len(numbers) - 12 + len(result) + 1):
			if numbers[i] > best_digit:
				best_digit = numbers[i]
				best_pos = i
		result.append(best_digit)
		start = best_pos + 1
	num = int("".join(str(d) for d in result))
	print(num)
	sum += num

print(sum)
