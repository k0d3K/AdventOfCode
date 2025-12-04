with open("input.txt", mode="r") as file:
	lines = file.readlines()

map = []
for line in lines:
	columns = list(line.strip())
	map.append(columns)

rows = len(map)
cols = len(map[0])

def checkCol(i, j):
	count = 0
	if i > 0 and map[j][i - 1] == '@':
		count += 1
	if map[j][i] == '@':
		count += 1
	if i < cols - 1 and map[j][i + 1] == '@':
		count += 1
	return count

def checkAround(i, j):
	count = -1
	if j > 0:
		count += checkCol(i, j - 1)
	count += checkCol(i, j)
	if j < rows - 1:
		count += checkCol(i, j + 1)
	return count

sum = 0
count = 1
while (count > 0):
	count = 0
	next_map = [row[:] for row in map]
	for j in range(rows):
		for i in range(cols):
			if map[j][i] == '@' and checkAround(i, j) < 4:
				next_map[j][i] = '.'
				count += 1
				sum += 1
	map = next_map

print(sum)
