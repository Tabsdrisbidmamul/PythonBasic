# json module  will allow us to save and retrieve python's data structures
import json

filename = 'favourite_numbers.json'

with open(filename) as f_obj:
	# we use the json.load method to load the contents of the json file to
	# variable fav nums
	# it goes json.load(ref) where ref is the reference to the filename in
	# the opening of the filename
	fav_nums = json.load(f_obj)

# output the contents
print('I know your favourite number, its ' + str(fav_nums))
