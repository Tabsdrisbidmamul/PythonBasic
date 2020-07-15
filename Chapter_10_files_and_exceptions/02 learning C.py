# file name held in variable
file = 'learning_python.txt'

# open the file and iterate through each line
with open(file) as file_object_2:
	for line in file_object_2:
		# the replace method will change the old string to the new string
		# .replace(old, new)
		# it does not change the string permanently, so it needs to be
		# stored in another variable
		new_line = line.replace('Python', 'C')
		print(new_line, end='')

