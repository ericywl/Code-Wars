def goodVsEvil(good, evil):
	good_list = []
	for number in good.split():
		good_list.append(int(number))
	evil_list = []
	for number in evil.split():
		evil_list.append(int(number))
	good_power = [1,2,3,3,4,10]
	evil_power = [1,2,2,2,3,5,10]
	good_total = 0
	evil_total = 0
	for g in range(len(good_list)):
	    good_total += good_list[g]*good_power[g]
	for e in range(len(evil_list)):
		evil_total += evil_list[e]*evil_power[e]

	print good_total
	print evil_total

	if good_total > evil_total:
		return "Battle Result: Good triumphs over Evil"
	elif evil_total > good_total:
		return "Battle Result: Evil eradicates all trace of Good"
	else:
		return "Battle Result: No victor on this battle field"