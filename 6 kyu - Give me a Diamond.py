def diamond(n):
	if n%2 != 0 and n > 0:
		expected = ""
		for i in range(1,n+1,2):
			expected = expected + " "*((n-i)/2) + "*"*i + "\n"
		for j in range(n-2,0,-2):
			expected = expected + " "*((n-j)/2) + "*"*j + "\n"
		return expected
	else:
		return None