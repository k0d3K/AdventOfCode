# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    part1.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: lguerbig <marvin@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/12/01 11:29:36 by lguerbig          #+#    #+#              #
#    Updated: 2024/12/04 07:13:31 by lguerbig         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

with open("input", 'r') as file:
    lines = file.readlines()

tab = []
for line in lines:
    columns = list(line.strip())
    tab.append(columns)

def find_nb_word(grid, word):
    directions = [
        (-1, 0),  # up
        (1, 0),   # down
        (0, -1),  # left
        (0, 1),   # right
        (-1, -1), # up-left
        (-1, 1),  # up-right
        (1, -1),  # down-left
        (1, 1)    # down-right
    ]
    
    rows = len(grid)
    cols = len(grid[0])
    word_len = len(word)

    def is_valid(x, y):
        return 0 <= x < rows and 0 <= y < cols

    def search(x, y, dx, dy):
        for i in range(word_len):
            nx = x + i * dx
            ny = y + i * dy
            if not is_valid(nx, ny) or grid[nx][ny] != word[i]:
                return False
        return True

    nb_words = 0

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == word[0]:
                for dx, dy in directions:
                    if search(i, j, dx, dy):
                        nb_words += 1

    return nb_words

print(find_nb_word(tab, "XMAS"))