def get_combo_value(operand, registers):
	if operand in [0, 1, 2, 3]:
		return operand
	elif operand == 4:
		return registers[0]
	elif operand == 5:
		return registers[1]
	elif operand == 6:
		return registers[2]

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
		print(opcode, operand)
		print("Register A: ", registers[0])
		print("Register B: ", registers[1])
		print("Register C: ", registers[2])
		print()
		print("Output: ", ",".join(map(str, output)))
		print()
	return ",".join(map(str, output))

with open('input', 'r') as file:
	A = int(file.readline().split(":")[1].strip())
	B = int(file.readline().split(":")[1].strip())
	C = int(file.readline().split(":")[1].strip())
	file.readline()
	program_line = file.readline().split(":")[1].strip()
	program = list(map(int, program_line.split(",")))
registers = [A, B, C]
result = run_program(registers, program)

print(result)
