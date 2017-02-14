def make_readable(seconds):
	hours = seconds/3600
	minutes = seconds%3600/60
	remainder = seconds%3600%60
	time = ['{:02}'.format(hours), '{:02}'.format(minutes), '{:02}'.format(remainder)]
	return ":".join(time)
