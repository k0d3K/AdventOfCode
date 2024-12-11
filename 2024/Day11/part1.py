# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    part1.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: lguerbig <marvin@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/12/01 11:29:36 by lguerbig          #+#    #+#              #
#    Updated: 2024/12/11 06:34:28 by lguerbig         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

stones = []
with open("input", 'r') as file:
	for line in file:
		stones = list(map(int, line.split(' ')))

def blink(stones):
	new_stones = []
	for stone in stones:
		if stone == 0:
			new_stones.append(1)
		elif len(str(stone)) % 2 == 0:
			s = str(stone)
			mid = len(s) // 2
			left, right = int(s[:mid]), int(s[mid:])
			new_stones.extend([left, right])
		else:
			new_stones.append(stone * 2024)
	return new_stones

for _ in range(75):
	stones = blink(stones)

print (len(stones))