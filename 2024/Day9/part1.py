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
			files.append(str(i // 2))

leftmost_free = 0
rightmost_file = len(files) - 1
while leftmost_free < len(files) and files[leftmost_free] != '.':
	leftmost_free += 1
while leftmost_free < rightmost_file:
	while rightmost_file > leftmost_free and files[rightmost_file] == '.':
		rightmost_file -= 1
	if rightmost_file > leftmost_free:
		files[leftmost_free], files[rightmost_file] = files[rightmost_file], '.'
		leftmost_free += 1
		while leftmost_free < len(files) and files[leftmost_free] != '.':
			leftmost_free += 1

sum = 0
for i in range(len(files)):
	if files[i] != '.':
		sum += i * int(files[i])

print (sum)