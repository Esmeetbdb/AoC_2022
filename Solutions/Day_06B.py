def find_start(s):
	for i in range(len(s)):
		marker = s[i:i+14]
		marker_set = set(marker)
		if len(marker_set) == 14:
			print(marker)
			print(i)
			print(s[i])
			print(i+14)
			print(s[i+14])
			break




for line in open('/mnt/c/Users/esmee/Documents/AoC_2022/PuzzleInput/Day_06.txt'):
	s = line.strip()
	find_start(s)
