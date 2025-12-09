with open("input.txt", mode="r") as file:
	lines = file.readlines()

tiles = []
for line in lines:
	x, y = line.strip().split(',')
	tiles.append((int(x), int(y)))

# cols = 0
# rows = 0
# for i, j in tiles:
# 	rows = max(rows, i)
# 	cols = max(cols, j)
# cols += 2
# rows += 2

# grid = [['#' if (i, j) in tiles else '.' for i in range(rows)] for j in range(cols)]

# for x in grid:
# 	print(x)

def calculate_square_erea(fisrt_corner, second_corner):
	x = fisrt_corner[0] - second_corner[0] + 1
	y = fisrt_corner[1] - second_corner[1] + 1
	return max(0, abs(x * y))

max_erea = 0
for fisrt_corner in tiles:
	for second_corner in tiles:
		erea = calculate_square_erea(fisrt_corner, second_corner)
		max_erea = max(max_erea, erea)

print(max_erea)