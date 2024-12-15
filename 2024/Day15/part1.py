
grid = []
moves = []
with open('input', 'r') as file:
	for line in file:
		if line[0] == '#':
			grid.append(list(line.strip()))
		else:
			for i in list(line.strip()):
				moves.append(i)

def find_start(grid):
	for j in range(len(grid)):
		for i in range(len(grid[0])):
			if grid[j][i] == '@':
				return i, j
	return 0, 0

def push(x, dx, y, dy):
	if grid[y + dy][x + dx] == '.':
		grid[y + dy][x + dx] = 'O'
		return 1
	if grid[y + dy][x + dx] == '#':
		return 0
	return push(x + dx, dx, y + dy, dy)

def move_robot(x, dx, y, dy):
	if push(x, dx, y, dy) == 1:
		grid[y + dy][x + dx] = '@'
		grid[y][x] = '.'
		return x + dx, y + dy
	return x, y

def make_right_move(x, y, move):
	#print (move)
	if move == '^':
		x, y = move_robot(x, 0, y, -1)
	if move == 'v':
		x, y = move_robot(x, 0, y, 1)
	if move == '<':
		x, y = move_robot(x, -1, y, 0)
	if move == '>':
		x, y = move_robot(x, 1, y, 0)
	# for row in grid:
	# 	print("".join(row) + "\n")
	return x, y

def boxes_coordonates(grid):
	sum = 0
	for j in range(len(grid)):
		for i in range(len(grid[0])):
			if grid[j][i] == 'O':
				sum += 100 * j + i 
	return sum


x, y = find_start(grid)
for move in moves:
	x, y = make_right_move(x ,y, move)
res = boxes_coordonates(grid)

with open("out", 'w') as file:
	for row in grid:
		file.write("".join(row) + "\n")

print (res)
