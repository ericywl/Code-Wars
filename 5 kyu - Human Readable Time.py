def make_readable(seconds):
	hours = seconds/3600
	minutes = seconds%3600/60
	remainder = seconds%3600%60
	time = ['{:02}:{:02}:{:02}'.format(hours,minutes,remainder)]
	return ":".join(time)
