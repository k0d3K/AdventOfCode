with open("input.txt", mode="r") as file:
	lines = file.readlines()

dial = 50
nb_zeros = 0

for line in lines:
	last_dial = dial
	number = int(line[1:])
	if line[0] == 'R':
		dial += number
	else:
		dial -= number
	while (dial > 99):
		if (dial != 100):
			nb_zeros += 1
		last_dial = dial
		dial -= 100
	while (dial < 0):
		if (last_dial != 0):
			nb_zeros += 1
		last_dial = dial
		dial += 100
	if (dial == 0):
		nb_zeros += 1

print("Total: ", nb_zeros)
