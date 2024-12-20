from collections import deque

def parse_maze(maze):
	start, end = None, None
	for r, row in enumerate(maze):
		for c, char in enumerate(row):
			if char == 'S':
				start = (r, c)
			elif char == 'E':
				end = (r, c)
	return start, end

def shortest_path(grid, start, end):
	rows, cols = len(grid), len(grid[0])
	directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
	queue = deque([(start, 0)])
	visited = set()
	visited.add(start)
	while queue:
		(x, y), time = queue.popleft()
		if (x, y) == end:
			return time
		for dx, dy in directions:
			nx, ny = x + dx, y + dy
			if 0 <= nx < rows and 0 <= ny < cols and (nx, ny) not in visited and grid[nx][ny] != "#":
				queue.append(((nx, ny), time + 1))
				visited.add((nx, ny))
	return -1

def find_cheats(grid, start, end):
	base_time = shortest_path(grid, start, end)
	rows, cols = len(grid), len(grid[0])
	cheats = []
	for r in range(rows):
		for c in range(cols):
			if grid[r][c] == "#":
				grid[r][c] = "."
				cheat_time = shortest_path(grid, start, end)
				grid[r][c] = "#"
				if cheat_time < base_time:
					cheats.append(base_time - cheat_time)
	return cheats

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
cheats = find_cheats(maze, start, end)
solution = sum(1 for cheat in cheats if cheat >= 100)

print(solution)
