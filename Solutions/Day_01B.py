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
	calo_list = list(Calories.values())
	calo_list.sort(reverse=True)
	print(sum(calo_list[0:3]))

CalorieCounter('/mnt/c/Users/esmee/Documents/AoC_2022/PuzzleInput/Day_01')
