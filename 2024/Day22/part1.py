def simulate_secret_number(number):

	tmp = number * 64
	number ^= tmp
	number %= 16777216

	tmp = number // 32
	number ^= tmp
	number %= 16777216

	tmp = number * 2048
	number ^= tmp
	number %= 16777216

	return number

initial_numbers = []
with open('input', 'r') as file:
	for line in file:
		initial_numbers.append(int(line))

sum = 0
for number in initial_numbers:
	for i in range(2000):
		next_number = simulate_secret_number(number)
		number = next_number
	print(number)
	sum += number


print(sum)
