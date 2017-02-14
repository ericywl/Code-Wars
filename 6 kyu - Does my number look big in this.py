def narcissistic(value):
	sum = 0
	power = len(str(value))
	for i in str(value):
		sum += int(i)**power

	if sum == value:
		return True
	else:
		return False