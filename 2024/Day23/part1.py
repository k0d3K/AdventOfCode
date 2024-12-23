connections = []
with open("input", mode="r") as file:
	for line in file:
		connections.append(tuple(line.strip().split('-')))

def link(connections):
	connected = set()
	for a, b in connections:
		for c, d in connections:
			if a in (c, d) or b in (c, d):
				if (a, c) in connections or (c, a) in connections:
					if (b, c) in connections or (c, b) in connections:
						connected.add(tuple(sorted([a, b, c])))
	return connected


def count_chiefs(connected):
	count = 0
	for conn in connected:
		for computeur in conn:
			if computeur[0] == "t":
				count += 1
				print(conn)
				break
	return count

connected = link(connections)
chiefs = count_chiefs(connected)

print(chiefs)