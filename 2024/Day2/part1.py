# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    part1.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: lguerbig <marvin@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/12/01 11:29:36 by lguerbig          #+#    #+#              #
#    Updated: 2024/12/02 09:04:55 by lguerbig         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def is_increasing(line):
    tmp = line[0]
    for i in range(1,len(line)):
        if line[i] <= tmp or line[i] - tmp > 3:
            return False
        tmp = line[i]
    return True

def is_decreasing(line):
    tmp = line[0]
    for i in range(1,len(line)):
        if line[i] >= tmp or tmp - line[i] > 3:
            return False
        tmp = line[i]
    return True

with open("input", mode="r") as file:
    lines = file.readlines()

tab = []
for line in lines:
    columns = list(map(int, line.split()))
    tab.append(columns)

nb_safe = 0
for line in tab:
    if is_increasing(line) or is_decreasing(line):
        nb_safe += 1
        print(line)

print(nb_safe)
