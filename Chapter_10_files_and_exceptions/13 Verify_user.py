import json


def get_stored_username():
	"""Get stored username if available"""
	filename = 'username.json'
	try:
		with open(filename) as f_obj:
			username = json.load(f_obj)
	except FileNotFoundError:
		return None
	else:
		return username


def get_new_username():
	"""Prompt for a new username"""
	username = input('What is your name? ')
	filename = 'username.json'
	with open(filename, 'w') as f_obj:
		json.dump(username, f_obj)
	return username


def verify_user():
	"""Validate whether this is the correct user"""
	username = get_stored_username()
	print('Are you ' + username + '?')
	user_input = input("Please enter either 'yes' or 'no': ")
	if user_input.lower() in ['y', 'yes']:
		return username
	elif user_input.lower in ['n', 'no']:
		return None
	else:
		print("Please enter either 'yes' or 'no\n")


def greet_user():
	"""Greet the user by name"""
	username = verify_user()
	if username:
		print('Welcome back, ' + username + '!')
	else:
		username = get_new_username()
		print('we\'ll remember you when you come back, ' + username + '!')


greet_user()
# this program will greet the user using refactored code split into
# functions to retrieve the username and output it from file
# or function to get a new user name and output a message saying that it was
#  acknowledged
