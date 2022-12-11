
def stacking(file):
	stacks = {}
	for line in open(file):
		if line.strip() == '':
			break
		for i in range(1,len(line)):
			#if line[i] == ' ':
			#	continue
			if line[i].isnumeric() == True:
				continue
			if (i) in stacks:
				stacks[(i)].append(line[i])
			else:
				stacks[(i)] = [line[i]]

	return stacks
stacks = stacking('/mnt/c/Users/esmee/Documents/AoC_2022/PuzzleInput/Day_05.txt')

for i in range(1,len(stacks)):
	print('{}: {}'.format(i, stacks[i]))
	print('\n')

