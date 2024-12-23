connections = []
with open("input", mode="r") as file:
	for line in file:
		connections.append(line.strip().split('-'))

def create_links(connections):
	links = {}
	for a, b in connections:
		if a not in links:
			links[a] = []
		if b not in links:
			links[b] = []
		links[a].append(b)
		links[b].append(a)
	return links

def expand_link(link, candidates, adj_list, linked):
	linked.append(link)
	for node in candidates.copy():
		new_candidates = candidates.intersection(adj_list[node])
		expand_link(link + [node], new_candidates, adj_list, linked)
		candidates.remove(node)

def find_linked(links):
	linked = []
	adj_list = {}
	for node, neighbors in links.items():
		adj_list[node] = set(neighbors)
	for node in links:
		candidates = set(links[node])
		expand_link([node], candidates, adj_list, linked)
	return linked

links = create_links(connections)
linked = find_linked(links)
largest_link = sorted(sorted(linked, key=len, reverse=True)[0])
print(",".join(largest_link))
