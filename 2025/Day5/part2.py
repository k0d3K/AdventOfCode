with open("test.txt", mode="r") as file:
	lines = file.readlines()

def countInRange(thisRange):
	return int(thisRange[1]) - int(thisRange[0]) + 1

def merge_ranges(ranges):
	merged = []
	for r in ranges:
		if not merged:
			merged.append(r)
		else:
			prev = merged[-1]
			if r[0] <= prev[1]:
				merged[-1] = (prev[0], max(prev[1], r[1]))
			else:
				merged.append(r)
	return merged

ranges = []

for line in lines:
	if line.strip() == "":
		break
	thisRange = line.strip().split('-')
	ranges.append((int(thisRange[0]), int(thisRange[1])))

ranges = sorted(ranges, key=lambda r: r[0])
ranges = merge_ranges(ranges)

sum = 0
for thisRange in ranges:
	sum += countInRange(thisRange)

print(sum)
