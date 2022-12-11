
def stacking(file):
	stacks = {}
	for line in open(file):
		if line.strip() == '':
			break
		for i in range(1,len(line),4):
			if line[i] == ' ':
				continue
			if line[i].isnumeric() == True:
				continue
			if (i//4+1) in stacks:
				stacks[(i//4+1)].append(line[i])
			else:
				stacks[(i//4+1)] = [line[i]]

	for line in open(file):
		if 'move' in line:
			content = line.strip().split(' ')
			amount = int(content[1])
			start = int(content[3])
			end = int(content[5])
			for i in range(amount):
				stacks[end].insert(0,stacks[start][0])
				stacks[start].pop(0)


	return stacks
stacks = stacking('/mnt/c/Users/esmee/Documents/AoC_2022/PuzzleInput/Day_05.txt')

for i in range(1,10):
	print('{}: {}'.format(i, stacks[i][0]))
	print('\n')

