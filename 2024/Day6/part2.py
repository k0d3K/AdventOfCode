with open("input", 'r') as file:
	lines = file.readlines()

map = []
for line in lines:
	columns = list(line.replace('\n', ''))
	map.append(columns)

x, y = 0, 0
for i in range(0, len(map)):
	for j in range(0, len(map[i])):
		if map[i][j] == '^':
			x, y = i, j
			break

directions = [
	(-1, 0),  # up
	(0, 1),   # right
	(1, 0),   # down
	(0, -1),  # left
]

def simu_guard(map, x, y):
	dir = 0
	visited_states = set()
	while  0 < x < len(map) - 1 and 0 < y < len(map[0]) - 1:
		if (x, y, dir) in visited_states:
			return True
		visited_states.add((x, y, dir))
		dx, dy = directions[dir]
		nx, ny = x + dx, y + dy
		if 0 <= nx < len(map) and 0 <= ny < len(map[0]) and map[nx][ny] != '#':
			x, y = nx, ny
		else:
			dir = (dir + 1) % 4
	return False

loop_positions = 0
for i in range(len(map)):
	for j in range(len(map[i])):
		if map[i][j] in ['#', '^']:
			continue
		map_with_obstacle = [row[:] for row in map]
		map_with_obstacle[i][j] = '#'
		if simu_guard(map_with_obstacle, x, y):
			loop_positions += 1

print(loop_positions)