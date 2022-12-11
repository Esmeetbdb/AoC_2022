import string
def find_priority(file):
	alphabet_1 = list(string.ascii_lowercase)
	alphabet_2 = list(string.ascii_uppercase)
	total_priorities = 0
	lines = []
	for line in open(file):
		lines.append(line.strip())
	for i in range(0,len(lines),3):
		list_group = lines[i:i+3]
		res = set(list_group[0]).intersection(set(list_group[1])).intersection(set(list_group[2]))
		for char in res:
			if char in alphabet_1:
				prio = 1+ alphabet_1.index(char)
			elif char in alphabet_2:
				prio = 27+ alphabet_2.index(char)
		total_priorities += prio
	print(total_priorities)

find_priority('../PuzzleInput/Day_03.txt')


