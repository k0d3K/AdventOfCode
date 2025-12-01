with open("input.txt", mode="r") as file:
	lines = file.readlines()

dial = 50
nb_zeros = 0

for line in lines:
	number = int(line[1:])
	if line[0] == 'R':
		dial += number
	else:
		dial -= number
	dial %= 100
	if dial == 0:
		nb_zeros += 1
		print("Total: ", nb_zeros)
	print(dial)

print("Total: ", nb_zeros)