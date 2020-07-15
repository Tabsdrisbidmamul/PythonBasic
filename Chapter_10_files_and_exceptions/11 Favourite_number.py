# json module  will allow us to save and retrieve python's data structures
import json

filename = 'favourite_numbers.json'
user_number = input('What is your favourite number? \n')

# open the file in write mode so we can store data to the file
with open(filename, 'w') as f_obj:
	# json.dump method allows us to store data in relation to the variable
	# and file reference
	# it goes json.dump(variable that holds the data, ref)
	# where ref is the reference to the filename in the opening of the filename
	json.dump(user_number, f_obj)
