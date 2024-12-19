def find_all_possible_paterns(design, towel_patterns):
	n = len(design)
	nb_possible_paterns = [0] * (n + 1)
	nb_possible_paterns[0] = 1 
	for i in range(1, n + 1):
		for pattern in towel_patterns:
			pattern_len = len(pattern)
			if i >= pattern_len and design[i - pattern_len:i] == pattern:
				nb_possible_paterns[i] += nb_possible_paterns[i - pattern_len]

	return nb_possible_paterns[n]

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
	nb_possible += find_all_possible_paterns(design, towel_patterns)

print(nb_possible)
