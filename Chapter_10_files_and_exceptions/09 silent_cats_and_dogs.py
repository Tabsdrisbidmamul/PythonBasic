# program to test try-except-else block with file reading


def read_file(filename):
	"""Read the contents of the file and print them to the screen"""
	# try to open the files as file object and read the contents of the file
	# and store it in contents
	try:
		with open(filename) as f_obj:
			contents = f_obj.read()
	# if file not found, fail silently
	except FileNotFoundError:
		pass
	# if except clause fails, then print the file to the screen
	else:
		print(contents)
	print()


# dog.txt file does not exist and will raise a exception error
file_1 = 'cats.txt'
file_2 = 'dogs.txt'

# call each function with the filename
read_file(file_1)
read_file(file_2)
