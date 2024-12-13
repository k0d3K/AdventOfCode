# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    part1.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: lguerbig <marvin@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/12/13 06:25:44 by lguerbig          #+#    #+#              #
#    Updated: 2024/12/13 07:42:38 by lguerbig         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import numpy as np
from math import gcd

def solve_equation(Ax, Ay, Bx, By, Px, Py):
	print(f"Solving system for: A=({Ax}, {Ay}), B=({Bx}, {By}), Prize=({Px}, {Py})")

	g1 = gcd(Ax, Bx)
	g2 = gcd(Ay, By)

	if Px % g1 != 0 or Py % g2 != 0:
		print(f"No solution: gcd check failed.")
		return None
	
	A = np.array([[Ax, Bx], [Ay, By]], dtype=int)
	B = np.array([Px, Py], dtype=int)

	try:
		solution = np.linalg.solve(A, B)

		if not np.allclose(solution, np.round(solution)):
			print(f"Solution is not integer: {solution}")
			return None

		a, b = np.round(solution).astype(int)
		cost = 3 * a + b
		print(f"Solution found: a={a}, b={b}, cost={cost}")
		return cost

	except np.linalg.LinAlgError:
		print("No solution: The system is singular.")
		return None

def solve_claw_machines(machines):
	"""Solve the claw machine problem for all machines."""
	total_tokens = 0
	prizes_won = 0

	for machine in machines:
		Ax, Ay = machine['A']
		Bx, By = machine['B']
		Px, Py = machine['prize']

		cost = solve_equation(Ax, Ay, Bx, By, Px, Py)
		if cost is not None:
			total_tokens += cost
			prizes_won += 1

	return prizes_won, total_tokens

machines = []
with open("test", 'r') as file:
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