from collections import defaultdict

def parse_racetrack(racetrack):
	start, end = None, None
	for r, row in enumerate(racetrack):
		for c, char in enumerate(row):
			if char == 'S':
				start = (r, c)
			elif char == 'E':
				end = (r, c)
	return start, end

def in_grid(i, c, N):
	return 0 <= i < N and 0 <= c < N

def find_path(grid, start, end):
	N = len(grid)
	directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
	path = [start]
	while path[-1] != end:
		r, c = path[-1]
		for dr, dc in directions:
			rr, cc = r + dr, c + dc
			if not in_grid(rr, cc, N):
				continue
			if len(path) > 1 and (rr, cc) == path[-2]:
				continue
			if grid[rr][cc] == "#":
				continue
			path.append((rr, cc))
			break
	return path

def calculate_times(path, normal_time):
	times = {}
	for t, coord in enumerate(path):
		times[coord] = normal_time - t
	return times

def find_cheats(grid, path, times, normal_time, max_len=20):
	N = len(grid)
	counts = defaultdict(int)
	saved = {}
	for t, coord in enumerate(path):
		r, c = coord
		for rr in range(r - max_len, r + max_len + 1):
			for cc in range(c - max_len, c + max_len + 1):
				time_used = abs(rr - r) + abs(cc - c)
				if not in_grid(rr, cc, N) or time_used > max_len or grid[rr][cc] == "#":
					continue
				rem_t = times[(rr, cc)]
				saved[(r, c, rr, cc)] = normal_time - (t + rem_t + time_used)
	return saved

def calculate_solution(saved):
	counts = defaultdict(int)
	res = 0
	for v in saved.values():
		if v >= 0:
			counts[v] += 1
		if v >= 100:
			res += 1
	return res

racetrack = []
with open('input', 'r') as file:
	for line in file:
		racetrack.append(list(line.strip()))

start, end = parse_racetrack(racetrack)
path = find_path(racetrack, start, end)
normal_time = len(path) - 1
times = calculate_times(path, normal_time)
saved = find_cheats(racetrack, path, times, normal_time)
solution = calculate_solution(saved)

print(solution)
