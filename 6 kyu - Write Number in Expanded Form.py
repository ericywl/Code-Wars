def expanded_form(num):
	power_10 = len(str(num)) - 1
	num_return = []
	for i in range(power_10,-1,-1):
		if num/(10**i) != 0:
			num_return.append(str((num/(10**i)) * (10**i)))
			num = num%(10**i)
	return " + ".join(num_return)

print expanded_form(70302)