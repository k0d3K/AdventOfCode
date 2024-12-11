# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    part1.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: lguerbig <marvin@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/12/01 11:29:36 by lguerbig          #+#    #+#              #
#    Updated: 2024/12/01 17:20:48 by lguerbig         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

with open("input", mode="r") as file:
    lines = file.readlines()

column1 = []
column2 = []
sum = 0

for line in lines:
    columns = line.split()
    if len(columns) == 2:
        column1.append(int(columns[0]))
        column2.append(int(columns[1]))

column1_sorted = sorted(column1)
column2_sorted = sorted(column2)

for i in range(0, len(column1_sorted)):
	sum += abs(column1_sorted[i] - column2_sorted[i])

print(sum)
