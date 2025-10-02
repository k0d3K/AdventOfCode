grid = []
with open("input", 'r') as file:
	for line in file:
		columns = list(map(int, line.strip()))
		grid.append(columns)

def find_trail(x, y, next_value, score):
	if next_value == 10:
		if trailtops[x][y] == 0:
			trailtops[x][y] = 1
			return score + 1
		else:
			return score
	if 0 <= x + 1 < len(grid) and grid[x + 1][y] == next_value:
		score = find_trail(x + 1, y, next_value + 1, score)
	if 0 <= x - 1 < len(grid) and grid[x - 1][y] == next_value:
		score = find_trail(x - 1, y, next_value + 1, score)
	if 0 <= y + 1 < len(grid[0]) and grid[x][y + 1] == next_value:
		score = find_trail(x, y + 1, next_value + 1, score)
	if 0 <= y - 1 < len(grid[0]) and grid[x][y - 1] == next_value:
		score = find_trail(x, y - 1, next_value + 1, score)
	return score

total_score = 0
for i in range(len(grid)):
	for j in range(len(grid[i])):
		if grid[i][j] == 0:
			trailtops = [[0] * len(grid[0]) for _ in range(len(grid))]
			total_score += find_trail(i, j, 1, 0)

print(total_score)