def comp(array1, array2):
	try:
		output = True
		if len(array1) == len(array2):
			for i in range(len(array1)):
				if sorted(array2)[i] == (sorted(array1)[i])**2:
					output = True
				else:
					output = False
					break
		else: 
			output = False
		return output
	except:
		return False
