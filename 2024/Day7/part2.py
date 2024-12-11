# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    part2.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: lguerbig <marvin@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2024/12/01 11:29:36 by lguerbig          #+#    #+#              #
#    Updated: 2024/12/07 20:57:46 by lguerbig         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

equations = []
with open("input", 'r') as file:
    for line in file:
        target, numbers = line.split(":")
        target = int(target.strip())
        numbers = list(map(int, numbers.strip().split()))
        equations.append((target, numbers))

def solve_equation(numbers, operators):
    result = numbers[0]
    for i in range(len(operators)):
        if operators[i] == '+':
            result += numbers[i + 1]
        elif operators[i] == '*':
            result *= numbers[i + 1]
        elif operators[i] == '||':
            result = int(str(result) + str(numbers[i + 1]))
    return result

def generate_operator_combinations(operators, current_combination, index, results):
    if index == len(current_combination):
        results.append(current_combination[:])
        return
    for op in operators:
        current_combination[index] = op
        generate_operator_combinations(operators, current_combination, index + 1, results)

sum = 0
for target, numbers in equations:
    num_positions = len(numbers) - 1
    operator_combinations = []
    generate_operator_combinations(['+', '*', '||'], [None] * num_positions, 0, operator_combinations)
    for ops in operator_combinations:
        if solve_equation(numbers, ops) == target:
            sum += target
            break

print (sum)