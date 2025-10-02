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

		for _dir, (dy, dx) in enumerate(dirs):
			ny, nx = y + dy, x + dx
			if 0 <= ny < rows and 0 <= nx < cols and maze[ny][nx] != "#" and (ny, nx) not in history:
				if _dir == curr_dir:
					queue.append(((ny, nx), history + [(ny, nx)], curr_score + 1, _dir))
				else:
					queue.append(((y, x), history + [], curr_score + 1000, _dir))
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

maze = []
with open('input', 'r') as file:
	for line in file:
		maze.append(list(line.strip()))

maze, start, end = prepare_maze(maze)
paths = find_paths(maze, start, end)
lowest_score = min(r[1] for r in paths)

print(lowest_score)
