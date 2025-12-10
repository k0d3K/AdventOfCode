import numpy as np
from itertools import product

with open("input.txt", mode="r") as file:
	lines = file.readlines()

def solve(A, B):
	n_buttons = A.shape[0]
	bests = None
	min_presses = n_buttons + 1

	for presses in product([0,1], repeat=n_buttons):
		presses = np.array(presses)
		result = np.mod(presses @ A, 2)
		if np.array_equal(result, B):
			weight = np.sum(presses)
			if weight < min_presses:
				min_presses = weight
				bests = presses.copy()

	return bests, min_presses

total = 0
for line in lines:
	result = line.strip().split()
	lights = []
	for i in result[0][1:-1]:
		lights.append(1 if i == '#' else 0)

	buttons = []
	for button in result[1:-1]:
		buttons.append([ 1 if str(x) in button.strip('()').split(',') else 0 for x in range(len(lights))])

	A = np.array(buttons)
	B = np.array(lights)

	print(A)
	print(B)

	solution, presses = solve(A, B)
	print(solution)
	total += presses

print(total)
