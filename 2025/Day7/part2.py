with open("input.txt", mode="r") as file:
	lines = file.readlines()

grid = [list(line.strip()) for line in lines]

nb_split = 0
positions = [0] * len(grid[0])
for i in range(len(grid[0])):
	if grid[0][i] == 'S':
		positions[i] += 1
print(positions)

for j in range(len(grid)):
	for i in range(len(positions)):
		if grid[j][i] == '^' and positions[i] > 0:
			nb_split = positions[i]
			positions[i] = 0
			positions[i - 1] += nb_split
			positions[i + 1] += nb_split
			print(positions)

sum = 0
for i in positions:
	sum += i

print(sum)