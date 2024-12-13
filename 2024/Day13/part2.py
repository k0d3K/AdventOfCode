# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    part2.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: lguerbig <marvin@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/12/13 06:25:44 by lguerbig          #+#    #+#              #
#    Updated: 2024/12/13 07:42:46 by lguerbig         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from sympy import symbols, Eq, solve
from math import gcd

def solve_equation(Ax, Ay, Bx, By, Px, Py):
	print(f"Solving system for: A=({Ax}, {Ay}), B=({Bx}, {By}), Prize=({Px}, {Py})")

	g1 = gcd(Ax, Bx)
	g2 = gcd(Ay, By)

	if Px % g1 != 0 or Py % g2 != 0:
		print(f"No solution: gcd check failed.")
		return None

	a, b = symbols('a b', integer=True)

	eq1 = Eq(Ax * a + Bx * b, Px)
	eq2 = Eq(Ay * a + By * b, Py)

	solution = solve((eq1, eq2), (a, b))

	if not solution:
		print("No integer solution found.")
		return None
	
	a_val = solution[a]
	b_val = solution[b]

	cost = 3 * a_val + b_val
	print(f"Solution found: a={a_val}, b={b_val}, cost={cost}")
	return cost


def solve_claw_machines(machines):
	"""Solve the claw machine problem for all machines."""
	total_tokens = 0
	prizes_won = 0

	for machine in machines:
		Ax, Ay = machine['A']
		Bx, By = machine['B']
		Px, Py = machine['prize']

		cost = solve_equation(Ax, Ay, Bx, By, Px + 10**13, Py + 10**13)
		if cost is not None:
			total_tokens += cost
			prizes_won += 1

	return prizes_won, total_tokens

machines = []
with open("input", 'r') as file:
	lines = file.readlines()
	for i in range(0, len(lines), 4):
		a_line = lines[i].strip()
		b_line = lines[i + 1].strip()
		prize_line = lines[i + 2].strip()

		ax, ay = map(int, a_line.split('X+')[1].split(', Y+'))
		bx, by = map(int, b_line.split('X+')[1].split(', Y+'))
		px, py = map(int, prize_line.split('X=')[1].split(', Y='))

		machines.append({'A': (ax, ay), 'B': (bx, by), 'prize': (px, py)})

prizes_won, total_tokens = solve_claw_machines(machines)
print("Prizes won:", prizes_won)
print("Total tokens used:", total_tokens)