def lose(opponent):
	if opponent == 'A':
		return 3
	elif opponent == 'B':
		return 1
	else:
		return 2

def draw(opponent):
	if opponent == 'A':
		return 1
	elif opponent == 'B':
		return 2
	else:
		return 3

def win(opponent):
	if opponent == 'A':
		return 2
	elif opponent == 'B':
		return 3
	else:
		return 1



def RPS_score(file):
	total_score = 0
	for line in open(file):
		content = line.strip().split(' ')
		round_score = 0
		if content[1] == 'X':
			round_score += lose(content[0])
		elif content[1] == 'Y':
			round_score += 3 + draw(content[0])
		elif content[1] == 'Z':
			round_score += 6 + win(content[0])

		total_score += round_score
	print(total_score)


RPS_score('/mnt/c/Users/esmee/Documents/AoC_2022/PuzzleInput/Day_02.txt')
