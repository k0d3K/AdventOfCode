# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    part2.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: lguerbig <marvin@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/12/02 09:01:59 by lguerbig          #+#    #+#              #
#    Updated: 2024/12/02 09:06:50 by lguerbig         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def can_be_safe_with_removal(line):
    for i in range(len(line)):
        modified_line = line[:i] + line[i+1:]
        if is_increasing(modified_line) or is_decreasing(modified_line):
            return True
    return False

def is_increasing(line):
    for i in range(1, len(line)):
        if line[i] <= line[i - 1] or line[i] - line[i - 1] > 3:
            return False
    return True

def is_decreasing(line):
    for i in range(1, len(line)):
        if line[i] >= line[i - 1] or line[i - 1] - line[i] > 3:
            return False
    return True

with open("input", mode="r") as file:
    lines = file.readlines()

tab = []
for line in lines:
    columns = list(map(int, line.split()))
    tab.append(columns)

nb_safe = 0
for line in tab:
    if is_increasing(line) or is_decreasing(line) or can_be_safe_with_removal(line):
        nb_safe += 1

print(nb_safe)