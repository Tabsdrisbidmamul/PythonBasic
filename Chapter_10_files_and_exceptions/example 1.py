# with will close the file once access to is no longer needed

# open function will open the file in its parenthesis and will look for it
# in the directory where the program is being currently executed

# close() function will close the file, but it is hard to know when to close
#  the file, as we don't want to close it too early, or have the data
# corrupted or lost!

with open('pi.txt') as file_object:
	content = file_object.read()
	# the .read() method will read the entire contents of the file and store
	#  it as one long string in the variable which we name 'contents'
	print(content)

# file paths, name the folder that is in the directory, backward slash it,
# and the name of the file

# a for loop will read the contents of the file
with open('text_files\pi_digits.txt') as file_object_1:
	for line in file_object_1:
		print(line)

# you can tell Python to find a file in a folder that is not in the
# directory where you're executing the program in
absolute_file_path = r"C:\Users\ricep\Desktop\Python\Lost_tears.txt"
with open(absolute_file_path) as file_object_2:
	for line in file_object_2:
		print(line)

# .readlines() method will takes each line from the file and stores it in a
# list
# then I just iterate through the list printing out each line, striping off
# whitespace and outputting the length of that string

filename = 'pi.txt'

with open(filename) as file_object_3:
	lines = file_object_3.readlines()

pi_string = ''
for line in lines:
	pi_string += line.strip()

print(pi_string)
print(len(pi_string))

# got million digits of pi into a text file with whitespace, then appended
# the lines to variable pi_string_2, and outputted it slicing so we print
# the first 50 decimal points and print the length of the list.

filename_2 = 'pi_million_digits.txt'

with open(filename_2) as file_object_4:
	lines = file_object_4.readlines()

pi_string_2 = ''
for line in lines:
	pi_string_2 += line.strip()

print(pi_string_2[:52])
print(len(pi_string_2))

birthday = input('Enter your birthday in ddmmyy: ')
if birthday in pi_string_2:
	print('your ' + birthday + 'is in the first million digits of pi')
else:
	print('maybe in the next million digits')
