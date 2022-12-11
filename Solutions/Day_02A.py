def lose(opponent,you):
	if opponent == 'A' and you == 'Z':
		return True
	elif opponent == 'B' and you == 'X':
		return True
	elif opponent == 'C' and you == 'Y':
		return True
	else:
		return False

def draw(opponent,you):
	if opponent == 'A' and you == 'X':
		return True
	elif opponent == 'B' and you == 'Y':
		return True
	elif opponent == 'C' and you == 'Z':
		return True
	else:
		return False

def RPS_score(file):
	total_score = 0
	for line in open(file):
		content = line.strip().split(' ')
		round_score = 0
		if content[1] == 'X':
			round_score += 1
		if content[1] == 'Y':
			round_score += 2
		if content[1] == 'Z':
			round_score += 3

		if lose(content[0],content[1]) == True:
			round_score += 0
		elif draw(content[0],content[1]) == True:
			round_score += 3
		else:
			round_score += 6
		total_score += round_score
	print(total_score)


RPS_score('/mnt/c/Users/esmee/Documents/AoC_2022/PuzzleInput/Day_02.txt')
