with open("test.txt", mode="r") as file:
	lines = file.readlines()

tiles = []
for line in lines:
	x, y = line.strip().split(',')
	tiles.append((int(x), int(y)))

cols = 0
rows = 0
for i, j in tiles:
	cols = max(cols, i)
	rows = max(rows, j)
cols += 2
rows += 2

grid = [['#' if (i, j) in tiles else '.' for i in range(cols)] for j in range(rows)]

for x in grid:
	print(x)
print()

### FOUND THE COUNTOUR ###

for (i, j) in tiles:
	for (x, y) in tiles:
		if i == x:
			for k in range(j + 1, y):
				grid[k][i] = 'X'
			for k in range(y + 1, j):
				grid[k][i] = 'X'
		if j == y:
			for k in range(i + 1, x):
				grid[j][k] = 'X'
			for k in range(x + 1, i):
				grid[j][k] = 'X'
		print("Contout", x, y)

for x in grid:
	print(x)
print()

### FILL THE COUNTOUR ###

directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def flood_fill(x, y):
	print("Flood", x, y)
	if x < 0 or x >= cols or y < 0 or y >= rows:
		return
	if grid[y][x] in ('#', "X", '-'):
		return
	grid[y][x] = '-'
	for (i, j) in directions:
		flood_fill(i + x, j + y)

flood_fill(0,0)

for x in grid:
	print(x)
print()

### FOUND THE MAXIMUM EREA ###

def hasOnlyGreenAndRedTiles(fisrt_corner, second_corner):
	for j in range(min(fisrt_corner[1], second_corner[1]), max(fisrt_corner[1] + 1, second_corner[1] + 1)):
		for i in range(min(fisrt_corner[0], second_corner[0]), max(fisrt_corner[0] + 1, second_corner[0] + 1)):
			if grid[j][i] == '-':
				return False
	return True

def calculate_square_erea(fisrt_corner, second_corner):
	x = fisrt_corner[0] - second_corner[0] + 1
	y = fisrt_corner[1] - second_corner[1] + 1
	return max(0, abs(x * y))

max_erea = 0
for fisrt_corner in tiles:
	for second_corner in tiles:
		if hasOnlyGreenAndRedTiles(fisrt_corner, second_corner):
			erea = calculate_square_erea(fisrt_corner, second_corner)
			max_erea = max(max_erea, erea)

print(max_erea)
