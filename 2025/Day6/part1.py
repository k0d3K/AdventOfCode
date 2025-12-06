with open("test.txt", mode="r") as file:
	lines = file.readlines()

equations = []
for line in lines:
	equations.append([x for x in line.strip().split(' ') if x])

symbols = equations.pop()

print(symbols)
result = [int(x) for x in equations[0]]
for i in range(1, len(equations)):
	for j in range(0, len(symbols)):
		if symbols[j] == '+':
			result[j] += int(equations[i][j])
		else:
			result[j] *= int(equations[i][j])
	print(result)

sum = 0
for i in result:
	sum += i

print(sum)
