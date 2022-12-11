import string
def find_priority(file):
	alphabet_1 = list(string.ascii_lowercase)
	alphabet_2 = list(string.ascii_uppercase)
	total_priorities = 0
	for line in open(file):
		list_a = []
		list_b = []
		for i in range(int(len(line.strip())/2)):
			list_a.append(line.strip()[i])
			list_b.append(line.strip()[int(len(line.strip())/2)+i])
		intersection = set(list_a) & set(list_b)
		for char in intersection:
			if char in alphabet_1:
				prio = 1+ alphabet_1.index(char)
			elif char in alphabet_2:
				prio = 27+ alphabet_2.index(char)
		total_priorities += prio
	print(total_priorities)
find_priority('../PuzzleInput/Day_03.txt')


