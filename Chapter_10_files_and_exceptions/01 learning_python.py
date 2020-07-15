# variable to hold file name
file = 'learning_python.txt'

# use open function to open file, and print the contents three times
with open(file) as file_object:
	content = file_object.read()
	print(content, '\n')
	print(content, '\n')
	print(content, '\n')

print('indent\n')

# open the file and read through each line and print it
with open(file) as file_object_2:
	for line in file_object_2:
		print(line, end="")

# open the file, read and store each line into a list, hold this list in lines
# iterate through lines appending it to indent_string to differentiate it
# from the previous work
with open(file) as file_object_3:
	lines = file_object_3.readlines()

print()
print()
indent_string = '(indent) '

for line in lines:
	print(indent_string + line, end='')
