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

def sort_update(update, rules):
	sorted_update = []
	remaining_pages = update[:]
	while remaining_pages:
		for page in remaining_pages:
			is_valid = True
			for x, y in rules:
				if y == page and x in remaining_pages:
					is_valid = False
					break
			if is_valid:
				sorted_update.append(page)
				remaining_pages.remove(page)
				break
		else:
			return []
	
	return sorted_update

def find_middle_pages_sum(updates, rules):
	sum = 0
	for update in updates:
		if not is_correct_order(update, rules):
			sorted_update = sort_update(update, rules)
			middle_idx = len(sorted_update) // 2
			sum += int(sorted_update[middle_idx])
	return sum

print(find_middle_pages_sum(updates, rules))
