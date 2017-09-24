def number2words(n):
	num_list = [x for x in str(n)]
	output_list = []
	digit_2 = num_digit_2(n, num_list)
	if n == 0:
		output = "zero"
	else:
		output_list.append(digit_2)
		output = " ".join(output_list)
	return output

def num_digit_2(n, num_list):
	digit2_list = num_list[-2:]
	m = len(digit2_list)
	digit2_wordList = [
				["ten", "eleven", "twelve", "thir", "four", "fif", "six", "seven", "eight", "nine"],
				["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"], 
				["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
				]
	if 9 < n < 13:
		output = digit2_wordList[0][int(digit2_list[-1])]
	elif 12 < n < 20:
		output = digit2_wordList[0][int(digit2_list[-1])] + "teen"
	else:
		output_list = [digit2_wordList[i][int(digit2_list[m-i])] for i in xrange(m, 0, -1)]
		output = "-".join(output_list)
	return output

print number2words(21)
print number2words(39)
print number2words(15)