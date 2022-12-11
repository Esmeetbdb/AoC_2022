def find_start(s):
	for i in range(len(s)):
		marker = s[i:i+4]
		marker_set = set(marker)
		if len(marker_set) == 4:
			print(marker)
			print(i)
			print(s[i])
			print(i+4)
			print(s[i+4])
			break




for line in open('../PuzzleInput/Day_06.txt'):
	s = line.strip()
	find_start(s)
