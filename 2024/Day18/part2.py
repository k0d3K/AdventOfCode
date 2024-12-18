from collections import deque

def shortest_path(grid, start, end):
	directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
	queue = deque([(start, 0)])
	visited = set()
	visited.add(start)
	while queue:
		(x, y), steps = queue.popleft()
		if (x, y) == end:
			return(steps)
		for dx, dy in directions:
			nx, ny = x + dx, y + dy
			if 0 <= nx < size and 0 <= ny < size and (nx, ny) not in visited and grid[ny][nx] == '.':
				queue.append(((nx, ny), steps + 1))
				visited.add((nx, ny))
	return -1

size = 71
start = (0, 0)
end = (size - 1, size - 1)
grid = [['.' for _ in range(size)] for _ in range(size)]

incoming_bytes = []
with open('input', 'r') as file:
	for line in file:
		x, y = map(int,line.strip().split(','))
		incoming_bytes.append((x, y))

for i in range(len(incoming_bytes)):
	x, y = incoming_bytes[i]
	grid[y][x] = '#'
	if (shortest_path(grid, start, end) == -1):
		print(x, y)
		break