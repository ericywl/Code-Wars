import string

def presses(phrase):
	input = phrase.upper()
	key_presses = 0
	reference = [" ","","ABC","DEF","GHI","JKL","MNO","PQRS","TUV","WXYZ","*","#"]
	for char in input:
		if char in string.digits:
			key_presses += (len(reference[int(char)]) + 1)
		else:
			for num in reference:
				if char in num:
					key_presses += (num.index(char)+1)

	return key_presses
