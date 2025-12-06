with open("input.txt", mode="r") as file:
	lines = file.readlines()

numbers = []
for j in range(len(lines) - 1):
	line = lines[j][:len(lines[j]) - 1]
	digits = [-1] * (len(line))
	for i in range(len(line)):
		if line[i] != ' ':
			digits[i] = int(line[i])
	numbers.append(digits)

symbols = lines[-1]

print(symbols)

def addAll(tab):
	result = 0
	for i in tab:
		result += i
	print("			", result)
	return result

def multyplyAll(tab):
	result = 1
	for i in tab:
		result *= i
	print("			", result)
	return result

print(numbers)

sum = 0
equations = []
for i in range(len(numbers[0]) - 1, -1, -1):
	number = 0
	for j in range(len(numbers)):
		if numbers[j][i] >= 0:
			number = 10 * number + numbers[j][i]
	if number > 0:
		equations.append(number)
	print(equations)
	symbol = symbols[i]
	if (symbol == '+'):
		sum += addAll(equations)
		equations = []
	if (symbol == '*'):
		sum += multyplyAll(equations)
		equations = []

print(sum)
