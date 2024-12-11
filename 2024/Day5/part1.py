# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    part1.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: lguerbig <marvin@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/12/01 11:29:36 by lguerbig          #+#    #+#              #
#    Updated: 2024/12/05 08:27:08 by lguerbig         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

with open("rules", 'r') as file:
    lines = file.readlines()

rules = []
for line in lines:
    columns =  line.replace('\n', '').split('|')
    rules.append(columns)

with open("updates", 'r') as file:
    lines = file.readlines()

updates = []
for line in lines:
    columns = line.replace('\n', '').split(',')
    updates.append(columns)

def is_correct_order(update, rules):
    position = {}
    for idx, page in enumerate(update):
        position[page] = idx
    for x, y in rules:
        if x in position and y in position and position[x] > position[y]:
            return False
    return True

def find_middle_pages_sum(updates, rules):
    sum = 0
    for update in updates:
        if is_correct_order(update, rules):
            middle_idx = len(update) // 2
            sum += int(update[middle_idx])
    return sum

def find_middle_pages(updates, rules):
    middle_pages = []
    for update in updates:
        if is_correct_order(update, rules):
            middle_idx = len(update) // 2
            middle_pages.append(update)
    return middle_pages

print(find_middle_pages_sum(updates, rules))
