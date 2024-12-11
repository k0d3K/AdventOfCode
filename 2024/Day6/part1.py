# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    part1.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: lguerbig <marvin@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/12/01 11:29:36 by lguerbig          #+#    #+#              #
#    Updated: 2024/12/06 07:44:03 by lguerbig         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

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

dir = 0
while  0 < x < len(map) - 1 and 0 < y < len(map[0]) - 1:
    dx, dy = directions[dir]
    nx, ny = x + dx, y + dy
    if 0 <= nx < len(map) and 0 <= ny < len(map[0]) and map[nx][ny] != '#':
        map[x][y] = 'X'
        x, y = nx, ny
    else:
        dir = (dir + 1) % 4

res = 1
for i in range(0, len(map)):
    for j in range(0, len(map[i])):
        if map[i][j] == 'X':
            res += 1

print (res)