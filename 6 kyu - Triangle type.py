def triangle_type(d, e, f):
	sides = sorted([d, e, f])
	a, b, c =  sides[0], sides[1], sides[2]
	if a + b > c:
		if a**2 + b**2 > c**2: 
			return 1
		elif a**2 + b**2 == c**2:
			return 2
		else:
			return 3
	else:
		return 0
