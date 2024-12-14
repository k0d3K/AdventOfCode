
def simulate_robots(robots, width, height, seconds):
	final_positions = []
	for (px, py), (vx, vy) in robots:
		new_x = (px + vx * seconds) % width
		new_y = (py + vy * seconds) % height
		final_positions.append((new_x, new_y))
	return final_positions

def count_quadrants(positions, width, height):
	mid_x, mid_y = width // 2, height // 2
	quadrants = [0, 0, 0, 0]

	for x, y in positions:
		if x == mid_x or y == mid_y:
			continue
		if x < mid_x and y < mid_y:
			quadrants[0] += 1
		elif x >= mid_x and y < mid_y:
			quadrants[1] += 1
		elif x < mid_x and y >= mid_y:
			quadrants[2] += 1
		elif x >= mid_x and y >= mid_y:
			quadrants[3] += 1

	return quadrants

def calculate_safety_factor(quadrants):
	factor = 1
	for count in quadrants:
		factor *= count
	return factor


robots = []
with open('input', 'r') as file:
	for line in file:
		position, velocity = line.split(" ")
		px, py = map(int, position[2:].split(","))
		vx, vy = map(int, velocity[2:].split(","))
		robots.append(((px, py), (vx, vy)))

WIDTH, HEIGHT = 101, 103
SECONDS = 100

final_positions = simulate_robots(robots, WIDTH, HEIGHT, SECONDS)
quadrants = count_quadrants(final_positions, WIDTH, HEIGHT)
safety_factor = calculate_safety_factor(quadrants)

print("Quadrants:", quadrants)
print("Safety Factor:", safety_factor)
