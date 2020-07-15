"""
Create a function that will take 2 parameters (to start with, the third
optional parameter is there to make sure that function still has full
functionality but also pass the unit test) that will ouput a neatly
formatted full name

"""

def get_formatted_name(first, last, middle=''):
	"""Generate a neatly formatted full name"""
	if middle:
		full_name = first + ' ' + middle + ' ' + last
	else:
		full_name = first + ' ' + last
	return full_name.title()