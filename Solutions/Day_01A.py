def CalorieCounter(file):
	Calories = {}
	i = 0
	Calories['Elf{}'.format(i)] = 0
	for line in open(file):
		content = line.strip()
		if content == '':
			i += 1
			Calories['Elf{}'.format(i)] = 0
			continue
		Calories['Elf{}'.format(i)] += int(content)
	print(max(Calories.values()))

CalorieCounter('../PuzzleInput/Day_01')
