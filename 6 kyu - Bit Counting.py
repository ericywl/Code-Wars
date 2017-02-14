def countBits(n):
	binary_list = []
	lp2 = 0

	for i in range(0, n):
		if n - 2**i < 0:
			lp2 = 2**(i-1)
			break
		elif n - 2**i == 0:
			lp2 = 2**i
			break

	while lp2 >= 1:
		if lp2 <= n:
			binary_list.append(1)
			n = n - lp2
			lp2 = lp2/2.0
		else:
			binary_list.append(0)
			lp2 = lp2/2.0

	return binary_list.count(1)

'''
 def countBits(n):
     return bin(n).count("1")
'''