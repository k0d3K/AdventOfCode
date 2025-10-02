map = []
with open("input", 'r') as file:
	for line in file:
		columns = list(line.strip())
		map.append(columns)

antinode = [line[:] for line in map]

def find_antinode(i, x, j, y):
	if (0 <= 2 * i - x < len(map) and 0 <= 2 * j - y < len(map[i])):
		antinode[2 * i - x][2 * j - y] = '#'
	if (0 <= 2 * x - i < len(map) and 0 <= 2 * y - j < len(map[i])):
		antinode[2 * x - i][2 * y - j] = '#'

def find_pairs(c, x, y):
	for i in range(len(map)):
		for j in range(len(map[i])):
			if map[i][j] == c and i != x and j != y:
				find_antinode(i, x, j, y)

for i in range(len(map)):
	for j in range(len(map[i])):
		if map[i][j] != '.':
			find_pairs(map[i][j], i, j)

sum = 0
for i in range(len(antinode)):
	for j in range(len(antinode[i])):
		if antinode[i][j] == '#':
			sum += 1

with open("out", 'w') as file:
	for row in antinode:
		file.write("".join(row) + "\n")
		
print (sum)