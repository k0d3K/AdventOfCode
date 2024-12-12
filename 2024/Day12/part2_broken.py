# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    part2.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: lguerbig <marvin@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/12/01 11:29:36 by lguerbig          #+#    #+#              #
#    Updated: 2024/12/12 16:08:46 by lguerbig         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

map = []
with open("test", 'r') as file:
	for line in file:
		map.append(list(line.strip()))

cpy_map = [line[:] for line in map]

rows = len(map)
cols = len(map[0])
directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

def new_border(r, c):
	if 0 <= r < rows and 0 <= c < cols:
		plant_type = cpy_map[r][c]
	if (r, c) in visited_border:
		if (r, c) not in visited_border_twice:
			return 1
	for dr, dc in directions:
		if (r + dr, c + dc) in visited_border:
			print(r, c, "because ", r + dr, c + dc)
			return 0
	for j in range(c, cols):
		if (r , j) in visited_border:
			print(r, c, "because ", r, j)
			return 0
		if 0 <= j < cols and 0 <= r < rows and 0 <= c < cols and cpy_map[r][j] != plant_type:
			break
	for j in range(c, 0):
		if (r , j) in visited_border:
			print(r, c, "because ", r, j)
			return 0
		if 0 <= j < cols and 0 <= r < rows and 0 <= c < cols and cpy_map[r][j] != plant_type:
			break
	for i in range(r, rows):
		if (i , c) in visited_border:
			print(r, c, "because ", i, c)
			return 0
		if  0 <= i < rows and 0 <= r < rows and 0 <= c < cols and cpy_map[i][c] != plant_type:
			break
	for i in range(r, 0):
		if (i , c) in visited_border:
			print(r, c, "because ", i, c)
			return 0
		if  0 <= i < rows and 0 <= r < rows and 0 <= c < cols and cpy_map[i][c] != plant_type:
			break
	print("	",r, c)
	visited_border_twice.append((r, c))
	return 1

def dfs(r, c, plant_type, dir):
	if 0 <= r < rows and 0 <= c < cols and (r, c) in visited:
		return 0, 0, 0
	if r < 0 or r >= rows or c < 0 or c >= cols or map[r][c] != plant_type:
		return 0, 1, 0
	map[r][c] = None
	visited.append((r, c))
	area, perimeter = 1, 0
	dir = (dir - 1) % 4
	for _ in range(4):
		(dr, dc) = directions[dir]
		sub_area, sub_perimeter, end = dfs(r + dr, c + dc, plant_type, dir)
		#print(r, c)
		area += sub_area
		if sub_perimeter == 1 and end == 0:
			perimeter += new_border(r + dr, c + dc)
			visited_border.append((r + dr, c + dc))
			print(r, c, "visited:", r + dr, c + dc)
		else:
			perimeter += sub_perimeter
		dir = (dir + 1) % 4
		print("		", perimeter)
	return area, perimeter, 1

data = []
for r in range(rows):
	for c in range(cols):
		if map[r][c] != None:
			print("new")
			visited = []
			borders = []
			visited_border = []
			visited_border_twice = []
			data.append([map[r][c], 0,0])
			area, perimeter, end = dfs(r, c, map[r][c], 0)
			data[-1][1] = area
			data[-1][2] = perimeter

price = 0
for set in data:
	print (set)
	price += set[1] * set[2]

print (price)