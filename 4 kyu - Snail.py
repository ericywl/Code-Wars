def snail(array):
	output = []
	while len(array) > 0:
		output += array[0]
		del array[0]

		if len(array) > 0:
			for i in array:
				output.append(i[-1])
				del i[-1]

			if array[-1]:
				output += array[-1][::-1]
				del array[-1]

			for i in reversed(array):
				output.append(i[0])
				del i[0]

	return output