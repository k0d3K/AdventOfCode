with open("input.txt", mode="r") as file:
	lines = file.readlines()

tiles = []
for line in lines:
	x, y = line.strip().split(',')
	tiles.append((int(x), int(y)))

verticals = set()
horizontals = set()
for (i, j) in tiles:
	for (x, y) in tiles:
		if i == x and j != y:
			verticals.add((x, min(j, y), max(j, y)))
		if j == y and i != x:
			horizontals.add((y, min(i, x), max(i, x)))
# print(verticals)
# print(horizontals)

def isInVerticals(x, y):
	for (access, min, max) in verticals:
		if access == x and min <= y and y <= max:
			# print("FOUND !! In vertivals x =", x, ",", y, " is in [", min, ":", max, "]")
			return True
	return False

def isRedInside(x, y):
	for (access, min, max) in horizontals:
		if access == y and min <= x and x <= max:
			# print("FOUND !! In horizontals y =", y, ",", x, " is in [", min, ":", max, "]")
			return True
	return False

def isVerticalBorderInsideSquare(border, c1, c2):
	# print("Check: ", border, c1, c2)
	x = border[0]
	if x > c1[0] and x < c2[0]:
		if border[1] < c1[1] and border[2] > c1[1]:
			return True
		if border[2] > c2[1] and border[1] < c2[1]:
			return True
		if border[1] >= c1[1] and border[2] <= c2[1]:
			return True
	return False

def isHorizontalBorderInsideSquare(border, c1, c2):
	# print("Check: ", border, c1, c2)
	y = border[0]
	if y > c1[1] and y < c2[1]:
		if border[1] < c1[0] and border[2] > c1[0]:
			return True
		if border[2] > c2[0] and border[1] < c2[0]:
			return True
		if border[1] >= c1[0] and border[2] <= c2[0]:
			return True
	return False

def cornerAccuracy(fisrt_corner, second_corner):
	if (fisrt_corner == second_corner):
		return
	c1 = (min(fisrt_corner[0], second_corner[0]), min(fisrt_corner[1], second_corner[1]))
	c2 = (max(fisrt_corner[0], second_corner[0]), max(fisrt_corner[1], second_corner[1]))
	for border in verticals:
		if isVerticalBorderInsideSquare(border, c1, c2):
			# print("INVALID VERTICAL: ", border, c1, c2)
			return False
	for border in horizontals:
		if isHorizontalBorderInsideSquare(border, c1, c2):
			# print("INVALID HORIZONTAL: ", border, c1, c2)
			return False
	# print("FOUND SOLUTION !!", fisrt_corner, second_corner )
	return True

def calculate_square_erea(fisrt_corner, second_corner):
	x = abs(fisrt_corner[0] - second_corner[0]) + 1
	y = abs(fisrt_corner[1] - second_corner[1]) + 1
	return max(0, x * y)

max_erea = 0
for i ,fisrt_corner in enumerate(tiles):
	for second_corner in tiles[i:]:
		if cornerAccuracy(fisrt_corner, second_corner):
			erea = calculate_square_erea(fisrt_corner, second_corner)
			max_erea = max(max_erea, erea)

print(max_erea)