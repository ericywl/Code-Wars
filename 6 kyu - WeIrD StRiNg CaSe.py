def to_weird_case(string):
	string_list = string.split(" ")
	weird_case = ""
	for word in string_list:
		for i in range(0,len(word)):
			if i%2 == 0:
				weird_case += word[i].upper()
			else:
				weird_case += word[i].lower()
		weird_case += " "
	return weird_case[:-1]