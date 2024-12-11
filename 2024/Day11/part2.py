# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    part2.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: lguerbig <marvin@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/12/11 08:11:53 by lguerbig          #+#    #+#              #
#    Updated: 2024/12/11 08:12:25 by lguerbig         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

dp = {}

def solve(n, count):
    if count == 0:
        return 1
    if (n, count) in dp:
        return dp[(n, count)]
    res = 0
    digits = str(n)
    if n == 0:
        res = solve(1, count - 1)
    elif len(digits) % 2 == 0:
        mid = len(digits) // 2
        left = int(digits[:mid])
        right = int(digits[mid:])
        res = solve(left, count - 1) + solve(right, count - 1)
    else:
        res = solve(n * 2024, count - 1)
    dp[(n, count)] = res
    return res

def fs(input_list, count):
    result = 0
    for digit in input_list:
        result += solve(digit, count)
    return result

stones = []
with open("input", 'r') as file:
	for line in file:
		stones = list(map(int, line.split(' ')))
num_blinks = 75

result = fs(stones, num_blinks)
print(result)
