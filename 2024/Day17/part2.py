def get_combo_value(operand, registers):
	if operand in [0, 1, 2, 3]:
		return operand
	elif operand == 4:
		return registers[0]
	elif operand == 5:
		return registers[1]
	elif operand == 6:
		return registers[2]
	# else:
	# 	raise ValueError(f"Invalid combo operand: {operand}")

def run_program(registers, program):
	output = []
	ip = 0  # Instruction pointer

	while ip < len(program):
		opcode = program[ip]
		operand = program[ip + 1]
		combo_value = get_combo_value(operand, registers)

		if opcode == 0:  # adv: A = A // (2 ** combo_value)
			registers[0] //= 2 ** combo_value
			ip += 2
		elif opcode == 1:  # bxl: B = B ^ operand (literal)
			registers[1] ^= operand
			ip += 2
		elif opcode == 2:  # bst: B = combo_value % 8
			registers[1] = combo_value % 8
			ip += 2
		elif opcode == 3:  # jnz: if A != 0, jump to operand (literal)
			if registers[0] != 0:
				ip = operand
			else:
				ip += 2
		elif opcode == 4:  # bxc: B = B ^ C
			registers[1] ^= registers[2]
			ip += 2
		elif opcode == 5:  # out: Output combo_value % 8
			output.append(combo_value % 8)
			ip += 2
		elif opcode == 6:  # bdv: B = A // (2 ** combo_value)
			registers[1] = registers[0] // (2 ** combo_value)
			ip += 2
		elif opcode == 7:  # cdv: C = A // (2 ** combo_value)
			registers[2] = registers[0] // (2 ** combo_value)
			ip += 2
		else:
			print(f"Unknown opcode: {opcode} at address {ip}")
			ip += 2
	return output

with open('input', 'r') as file:
	A = int(file.readline().split(":")[1].strip())
	B = int(file.readline().split(":")[1].strip())
	C = int(file.readline().split(":")[1].strip())
	file.readline()
	program_line = file.readline().split(":")[1].strip()
	program = list(map(int, program_line.split(",")))


# Some value of A make a consant lenght result, so we're focusing on them
A = sum(7 * 8**i for i in range(len(program) - 1)) + 1
i = 0
while 1:
	result = run_program([A, B, C], program)
	
	if (result == program):
		break

	add = 0
	for i in range(len(result) - 1, -1, -1):
		if result[i] != program[i]:
			add = 8**i
			A += add
			break
	print (A)
