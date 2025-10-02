with open("input", 'r') as file:
	lines = file.readlines()

tab = []
for line in lines:
	columns = list(line.strip())
	tab.append(columns)

def find_nb_X_word(grid, word):
	directions = [
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
						if grid[i + (word_len - 1) * dx][j] == word[0]:
							if search(i + (word_len - 1) * dx , j, -dx, dy):
								nb_words += 1
						elif grid[i][j + (word_len - 1) * dy] == word[0]:
							if search(i , j + (word_len - 1) * dy, dx, -dy):
								nb_words += 1
	return int(nb_words / 2)

print(find_nb_X_word(tab, "MAS"))