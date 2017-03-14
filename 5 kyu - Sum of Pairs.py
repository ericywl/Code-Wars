def sum_pairs(ints, s):
	n = len(ints)
	m = {}
	for i in range(n):
		if s-ints[i] in m:
			return [s-ints[i], ints[i]]
		if ints[i] not in m:
			m[ints[i]] = i
	return None

print sum_pairs([4, 3, 2, 3, 4], 6)
