def is_possible(design, towel_patterns):
	for pattern in towel_patterns:
		if design[:len(pattern)] == pattern:
			if is_possible(design[len(pattern):], towel_patterns):
				return True
			if not design[len(pattern):]:
				return True
	return False

towel_patterns = []
designs = []

with open('input', 'r') as file:
	for line in file:
		if ',' in line:
			towel_patterns = [pattern.strip() for pattern in line.strip().split(',')]
		elif line.strip():
			designs.append(line.strip())

nb_possible = 0
for design in designs:
	if is_possible(design, towel_patterns):
		nb_possible += 1

print(nb_possible)
