with open("input.txt", mode="r") as file:
	lines = file.readlines()

grid = [list(line.strip()) for line in lines]

nb_split = 0
positions = set()
debug = [row for row in grid]
for i in range(len(grid[0])):
	if grid[0][i] == 'S':
		positions.add(i)

for j in range(len(grid)):
	next_positions = set(positions)
	for i in positions:
		if grid[j][i] == '^':
			nb_split += 1
			next_positions.remove(i)
			next_positions.add(i - 1)
			next_positions.add(i + 1)
		else:
			debug[j][i] = '|'
	positions = next_positions
	print(debug[j])

print(nb_split)