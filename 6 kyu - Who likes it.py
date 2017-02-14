def likes(names):
	string = "likes this"
	if not names:
		return "no one likes this"
	else:
		for people in names:
			return people, string

print likes(["Peter"])