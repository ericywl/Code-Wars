def bouncingBall(h, bounce, window):
	if 0 < bounce < 1 and h > 0 and h > window:
		see_count = 1
		h = h*bounce
		while h > window:
			h = h*bounce
			see_count += 2
		return see_count
	else:
		return -1