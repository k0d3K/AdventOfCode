from math import sqrt

with open("input.txt", mode="r") as file:
	lines = file.readlines()

def norm(x, y, z):
	return sqrt(x*x + y*y + z*z)

size = len(lines)
distances = [[0 for _ in range(size)] for _ in range(size)]
boxes = [[int(x) for x in line.strip().split(',')] for line in lines]

# for box in boxes:
# 	print(box)

for i in range(len(boxes)):
	for j in range(len(boxes)):
		distances[i][j] = norm(boxes[i][0] - boxes[j][0], boxes[i][1] - boxes[j][1], boxes[i][2] - boxes[j][2])

links = list(set())

def union(links, a, b):
	set1 = None
	set2 = None

	for s in links:
		if a in s:
			set1 = s
		if b in s:
			set2 = s
	if set1 is None and set2 is None:
		links.append({a, b})
	elif set1 is not None and set2 is None:
		set1.add(b)
	elif set1 is None and set2 is not None:
		set2.add(a)
	elif set1 is not set2:
		set1 |= set2
		links.remove(set2)

maximum = 0
for dist in distances:
	if max(dist) > maximum:
		maximum = max(dist)

nb_links = 1000

while nb_links > 0:
	minimum = maximum
	box1 = 0
	box2 = 0
	for i in range(len(boxes)):
		for j in range(i + 1, len(distances[i])):
			if distances[i][j] > 0 and distances[i][j] < minimum:
				minimum = distances[i][j]
				box1 = i
				box2 = j
	distances[box1][box2] = 0 #mark this box as linked
	distances[box2][box1] = 0 #mark this box as linked | not sure this is usefull
	# print("min :", box1, box2, boxes[box1], boxes[box2], minimum)
	union(links, box1, box2)
	# print(links, len(links))
	print(len(links))
	nb_links -= 1

sizes = [len(link) for link in links]
sizes.sort(reverse=True)

total = 1
for i in range(3):
	total *= sizes[i]

print(total)