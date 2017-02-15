def solution(digits):
	length = len(str(digits))
	largest_num = 0
	for i in range(length-4):
		if int(digits[i:i+5]) >= largest_num:
			largest_num = int(digits[i:i+5])
	return largest_num
