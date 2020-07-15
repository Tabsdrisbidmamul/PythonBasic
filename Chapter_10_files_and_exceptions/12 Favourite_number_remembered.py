import json

filename = 'favourite_numbers.json'

# this is programs 11 and 11.5 combined together using a try-except-else block
try:
	with open(filename) as f_obj:
		fav_nums = json.load(f_obj)
except FileNotFoundError:
	user_number = input('What is your favourite number? \n')
	with open(filename, 'w') as f_obj:
		json.dump(user_number, f_obj)
else:
	print('I know your favourite number, its ' + str(fav_nums))
