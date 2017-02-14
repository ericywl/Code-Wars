def likes(names):
	string1 = "likes this"
	string2 = "like this"
	people = ""
	if not names:
		return "no one likes this"
	else:
		if len(names) == 1:
			people = "".join(names)
			return people + " " + string1
		else:	
			if len(names) == 2:
				people = " and ".join(names)
			elif len(names) == 3:
				people = names[0] + ", " + names[1] + " and " + names[2]
			else:
				people = names[0] + ", " + names[1] + " and " + str(len(names)-2) + " others"
		return people + " " + string2