map = []
with open("input", 'r') as file:
	for line in file:
		map.append(list(line.strip()))

rows = len(map)
cols = len(map[0])

def dfs(map, r, c, plant_type):
	if 0 <= r < rows and 0 <= c < cols and (r, c) in visited:
		return 0, 0
	if r < 0 or r >= rows or c < 0 or c >= cols or map[r][c] != plant_type:
		return 0, 1
	map[r][c] = None
	visited.append((r, c))
	area, perimeter = 1, 0
	for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
		sub_area, sub_perimeter = dfs(map, r + dr, c + dc, plant_type)
		area += sub_area
		perimeter += sub_perimeter
	return area, perimeter

data = []
for r in range(rows):
	for c in range(cols):
		if map[r][c] is not None:
			visited = []
			data.append([map[r][c], 0,0])
			area, perimeter = dfs(map, r, c, map[r][c])
			data[-1][1] = area
			data[-1][2] = perimeter

price = 0
for set in data:
	price += set[1] * set[2]

print (price)