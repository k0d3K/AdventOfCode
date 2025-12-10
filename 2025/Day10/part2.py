import pulp as pl

with open("input.txt", mode="r") as file:
	lines = file.readlines()

# Mixed Integer Programming with PuLP
# https://or.engineeringcodehub.com/en/latest/MIP/tutorials/PuLP%20and%20Python%20MIP%20Tutorial.html

def solve(buttons, joltage):
	nb_buttons = len(buttons)
	nb_joltage = len(joltage)

	# Create the model
	model = pl.LpProblem("Minimum_presses", pl.LpMinimize)
	# Define decision variables
	x = [pl.LpVariable(f"x{i}", lowBound=0, cat=pl.LpInteger) for i in range(nb_buttons)]
	# Define objective : minimize total presses
	model += pl.lpSum(x)
	# Constraints: Each counter must reach there voltage
	for j in range(nb_joltage):
		model += pl.lpSum(buttons[i][j] * x[i] for i in range(nb_buttons)) == joltage[j]
	# Solve the problem
	model.solve(pl.PULP_CBC_CMD(msg=False))

	return [int(pl.value(i)) for i in x]

total = 0
for line in lines:
	result = line.strip().split()
	joltage = [int(x) for x in result[-1][1:-1].split(',')]

	buttons = []
	for button in result[1:-1]:
		buttons.append([ 1 if str(x) in button.strip('()').split(',') else 0 for x in range(len(joltages))])

	print(buttons)
	print(joltage)

	solution = solve(buttons, joltage)
	print(solution)
	total += sum(solution)

print(total)
