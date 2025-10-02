with open("input", mode="r") as file:
	lines = file.readlines()

column1 = []
column2 = []
sum = 0

for line in lines:
	columns = line.split()
	if len(columns) == 2:
		column1.append(int(columns[0]))
		column2.append(int(columns[1]))

for i in column1:
	for j in column2:
		if (i == j):
			sum += i

print(sum)