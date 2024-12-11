# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    part2.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: lguerbig <marvin@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/12/01 11:29:36 by lguerbig          #+#    #+#              #
#    Updated: 2024/12/09 07:46:32 by lguerbig         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

memory = []
with open("input", 'r') as file:
	for line in file:
		memory = list(map(int, line.strip()))

files = []
for i in range(len(memory)):
	if i % 2:
		for count in range(memory[i]):
			files.append('.')
	else:
		for count in range(memory[i]):
			files.append(i // 2)

def find_free_spans(files):
	spans = []
	start = None
	for i, block in enumerate(files):
		if block == '.':
			if start is None:
				start = i
		elif start is not None:
			spans.append((start, i - start))
			start = None
	if start is not None:
		spans.append((start, len(files) - start))
	return spans


max_file_id = max(block for block in files if block != '.')
for file_id in range(max_file_id, -1, -1):
	file_indices = []
	for i, block in enumerate(files):
		if block == file_id:
			file_indices.append(i)

	file_length = len(file_indices)
	free_spans = find_free_spans(files)

	for start, length in free_spans:
		if length >= file_length and start < file_indices[0]:
			for i in range(file_length):
				files[start + i] = file_id
			for i in file_indices:
				files[i] = '.'
			break

sum = 0
for i in range(len(files)):
	if files[i] != '.':
		sum += i * int(files[i])

print (sum)