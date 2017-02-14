def tickets(people):
	ticket_change = {100:75, 50:25, 25:0}
	change_amt = {100:0, 50:0, 25:0}
	ans = ""
	for money in people:
		change_amt[money] += 1
		if money == 100 and change_amt[50] >= 1 and change_amt[25] >= 1:
			ans = "YES"
			change_amt[50] -= 1
			change_amt[25] -= 1
		elif money == 100 and change_amt[50] == 0 and change_amt[25] >= 3:
			ans = "YES"
			change_amt[25] -= 3
		elif money == 50 and change_amt[25] >= 1:
			ans = "YES"
			change_amt[25] -= 1
		elif money == 25:
			ans = "YES"
		else:
			ans = "NO"
	return ans