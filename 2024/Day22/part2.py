def simulate_secret_number(number):

	tmp = number * 64
	number ^= tmp
	number %= 16777216

	tmp = number // 32
	number ^= tmp
	number %= 16777216

	tmp = number * 2048
	number ^= tmp
	number %= 16777216

	return number

def generate_prices_and_changes(initial_number):
	prices = []
	current_number = initial_number
	for _ in range(2000):
		current_number = simulate_secret_number(current_number)
		prices.append(current_number % 10)
	
	changes = [prices[i] - prices[i - 1] for i in range(1, len(prices))]
	return prices, changes

def find_best_sequence(initial_numbers):
	sequence_to_bananas = {}

	for initial_number in initial_numbers:
		prices, changes = generate_prices_and_changes(initial_number)

		seen_sequences = set()

		for i in range(len(changes) - 3):
			sequence = tuple(changes[i:i+4])

			if sequence not in seen_sequences:
				seen_sequences.add(sequence)

				if sequence not in sequence_to_bananas:
					sequence_to_bananas[sequence] = 0

				sequence_to_bananas[sequence] += prices[i+4]

	best_sequence = max(sequence_to_bananas, key=sequence_to_bananas.get)
	max_bananas = sequence_to_bananas[best_sequence]

	return best_sequence, max_bananas

initial_numbers = []
with open('input', 'r') as file:
	for line in file:
		initial_numbers.append(int(line))

best_sequence, max_bananas = find_best_sequence(initial_numbers)

print("Best sequence:", best_sequence)
print("Max bananas:", max_bananas)
