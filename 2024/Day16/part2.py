def parse_maze(maze):
	start, end = None, None
	for r, row in enumerate(maze):
		for c, char in enumerate(row):
			if char == 'S':
				start = (r, c)
			elif char == 'E':
				end = (r, c)
	return start, end

def find_paths(maze, start, end):
	rows, cols = len(maze), len(maze[0])

	dirs = [(0, 1), (-1, 0), (0, -1), (1, 0)]
	paths = []
	visited = {}

	queue = [(start, [start], 0, 0)]
	while queue:
		(y, x), history, curr_score, curr_dir = queue.pop(0)

		if (y, x) == end:
			paths.append((history, curr_score))
			continue

		if ((y, x), curr_dir) in visited and visited[((y, x), curr_dir)] < curr_score:
			continue

		visited[((y, x), curr_dir)] = curr_score

		for new_dir, (dy, dx) in enumerate(dirs):
			ny, nx = y + dy, x + dx
			if 0 <= ny < rows and 0 <= nx < cols and maze[ny][nx] != "#" and (ny, nx) not in history:
				if new_dir == curr_dir:
					queue.append(((ny, nx), history + [(ny, nx)], curr_score + 1, new_dir))
				else:
					queue.append(((y, x), history + [], curr_score + 1000, new_dir))
	return paths

def prepare_maze(input_maze):
	start = None
	end = None
	for i in range(len(input_maze)):
		for j in range(len(input_maze[i])):
			if input_maze[i][j] == 'S':
				start = (i, j)
				input_maze[i][j] = '.'
			elif input_maze[i][j] == 'E':
				end = (i, j)
				input_maze[i][j] = '.'
	return input_maze, start, end

def add_solutions(maze, solutions):
	maze_copy = [row[:] for row in maze]
	for solution, score in solutions:
		for x, y in solution:
			if maze_copy[x][y] == '.':
				maze_copy[x][y] = 'O'
	return maze_copy

maze = []
with open('input', 'r') as file:
	for line in file:
		maze.append(list(line.strip()))

maze, start, end = prepare_maze(maze)
paths = find_paths(maze, start, end)
lowest_score = min(r[1] for r in paths)
solutions = [r for r in paths if r[1] == lowest_score]
completed_maze = add_solutions(maze, solutions)

with open('out', 'w') as file:
	for row in completed_maze:
		file.write(''.join(str(cell) for cell in row))
		file.write('\n')

nb_tiles = 0
for row in completed_maze:
	for cell in row:
		if cell == 'O':
			nb_tiles += 1

print(nb_tiles)
