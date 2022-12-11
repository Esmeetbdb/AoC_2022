def test_overlapping(list_1,list_2):
	if int(list_1[1]) < int(list_2[0]) or int(list_1[0]) > int(list_2[1]):
		return True
	else:
		return False 

def check_overlap(file):
	counter = 0
	for line in open(file):
		content = line.strip().split(',')
		elf_1 = content[0].split('-')
		elf_2 = content[1].split('-')
		if test_overlapping(elf_1, elf_2) == False:
			counter += 1
		elif test_overlapping(elf_2, elf_1) == False:
			counter += 1
	print(counter)

check_overlap('../PuzzleInput/Day_04.txt')
