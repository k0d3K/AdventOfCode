# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    part2.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: lguerbig <marvin@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/12/01 11:29:36 by lguerbig          #+#    #+#              #
#    Updated: 2024/12/08 07:39:25 by lguerbig         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

map = []
with open("input", 'r') as file:
	for line in file:
		columns = list(line.strip())
		map.append(columns)

antinode = [line[:] for line in map]

def find_antinode(i, x, j, y):
	max_factor = max(len(map), len(map[0]))
	for factor in range(0, max_factor):
		if (0 <= i + factor * (i - x) < len(map) and 0 <= j + factor * (j - y)  < len(map[i])):
			antinode[i + factor * (i - x) ][j + factor * (j - y) ] = '#'
		if (0 <= x + factor * (x - i)  < len(map) and 0 <= y + factor * (y - j)  < len(map[i])):
			antinode[x + factor * (x - i) ][y + factor * (y - j) ] = '#'

def find_pairs(c, x, y):
	for i in range(len(map)):
		for j in range(len(map[i])):
			if map[i][j] == c and i != x and j != y:
				find_antinode(i, x, j, y)

for i in range(len(map)):
	for j in range(len(map[i])):
		if map[i][j] != '.':
			find_pairs(map[i][j], i, j)

sum = 0
for i in range(len(antinode)):
	for j in range(len(antinode[i])):
		if antinode[i][j] == '#':
			sum += 1

with open("out", 'w') as file:
    for row in antinode:
        file.write("".join(row) + "\n")

print (sum)