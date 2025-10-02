grid = []
moves = []
with open('input', 'r') as file:
	for line in file:
		if line[0] == '#':
			new_line = []
			for i in list(line.strip()):
				if i == '#':
					new_line.append('#')
					new_line.append('#')
				if i == 'O':
					new_line.append('[')
					new_line.append(']')
				if i == '.':
					new_line.append('.')
					new_line.append('.')
				if i == '@':
					new_line.append('@')
					new_line.append('.')
			grid.append(new_line)
		else:
			for i in list(line.strip()):
				moves.append(i)

file = open("out", 'w')

def find_start(grid):
	for j in range(len(grid)):
		for i in range(len(grid[0])):
			if grid[j][i] == '@':
				return i, j
	return 0, 0

def check_push_vertical(x, y, dy):
	if grid[y + dy][x] == '.':
		return 1
	if grid[y + dy][x] == '#':
		return 0
	if grid[y + dy][x] == '[':
		return check_push_vertical(x, y + dy, dy) and check_push_vertical(x + 1, y + dy, dy)
	if grid[y + dy][x] == ']':
		return check_push_vertical(x, y + dy, dy) and check_push_vertical(x - 1, y + dy, dy)

def push_vertical(x, y, dy):
	if grid[y + dy][x] == '.':
		return 1
	if grid[y + dy][x] == '#':
		return 0
	if grid[y + dy][x] == '[':
		if push_vertical(x, y + dy, dy) and push_vertical(x + 1, y + dy, dy):
			grid[y + 2*dy][x] = '['
			grid[y + 2*dy][x + 1] = ']'
			grid[y + dy][x] = '.'
			grid[y + dy][x + 1] = '.'
			return 1
		return 0
	if grid[y + dy][x] == ']':
		if push_vertical(x, y + dy, dy) and push_vertical(x - 1, y + dy, dy):
			grid[y + 2*dy][x] = ']'
			grid[y + 2*dy][x - 1] = '['
			grid[y + dy][x] = '.'
			grid[y + dy][x - 1] = '.'
			return 1
		return 0

def check_push_horizontal(x, y, dx):
	if grid[y][x + dx] == '.':
		return 1
	if grid[y][x + dx] == '#':
		return 0
	if grid[y][x + dx] == '[':
		return check_push_horizontal(x + 2*dx, y, dx)
	if grid[y][x + dx] == ']':
		return check_push_horizontal(x + 2*dx, y, dx)

def push_horizontal(x, y, dx):
	if grid[y][x + dx] == '.':
		return 1
	if grid[y][x + dx] == '#':
		return 0
	if grid[y][x + dx] == '[':
		if push_horizontal(x + 2*dx, y, dx):
			grid[y][x + 2*dx] = '['
			grid[y][x + 2*dx + 1] = ']'
			grid[y][x] = '.'
			grid[y][x + 1] = '.'
			return 1
		return 0
	if grid[y][x + dx] == ']':
		if push_horizontal(x + 2*dx, y, dx):
			grid[y][x + 2*dx] = ']'
			grid[y][x + 2*dx - 1] = '['
			grid[y][x] = '.'
			grid[y][x - 1] = '.'
			return 1
		return 0

def move_robot(x, dx, y, dy):
	if dx:
		if check_push_horizontal(x, y, dx) == 1:
			push_horizontal(x, y, dx)
			grid[y + dy][x + dx] = '@'
			grid[y][x] = '.'
			return x + dx, y + dy
	elif dy:
		if check_push_vertical(x, y, dy) == 1:
			push_vertical(x, y, dy)
			grid[y + dy][x + dx] = '@'
			grid[y][x] = '.'
			return x + dx, y + dy
	return x, y

def make_right_move(x, y, move):
	file.write(move)
	if move == '^':
		x, y = move_robot(x, 0, y, -1)
	if move == 'v':
		x, y = move_robot(x, 0, y, 1)
	if move == '<':
		x, y = move_robot(x, -1, y, 0)
	if move == '>':
		x, y = move_robot(x, 1, y, 0)
	for row in grid:
		file.write("".join(row) + "\n")
	return x, y

def boxes_coordonates(grid):
    total = 0
    for j in range(len(grid)):
        for i in range(len(grid[0])):
            if grid[j][i] == '[':
                total += 100 * j + i
    return total

x, y = find_start(grid)
for move in moves:
	x, y = make_right_move(x ,y, move)
res = boxes_coordonates(grid)

print (res)