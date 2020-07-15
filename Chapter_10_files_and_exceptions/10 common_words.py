# program that will dracula.txt to count how many times dracula appears

file_1 = 'dracula.txt'

with open(file_1) as f_obj:
	contents = f_obj.read()
	# by using the .lower() method it will nullify case sensitive forms of
	# dracula

	# the .count() method will count the number of times a word appears in
	# the file
	num_of_times = contents.lower().count('dracula')
	print(num_of_times)
