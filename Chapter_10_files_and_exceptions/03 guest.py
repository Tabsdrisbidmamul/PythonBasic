# a program that will ask the user for their name and save into a text file
# variable indicates the file name
filename = 'programming.txt'

# ask the user name and store it into username
userName = str(input('What is your name? '))

# call the open function, with variable name and use the write mode to write
# into file
with open(filename, 'w') as file_object:
	# use the .wrtie method, and it accepts arguments as strings only
	file_object.write(userName)

# if the file does not exist, python will create a file called it,
# if it does python will overwrite the current contents
# the write mode will always overwrite the file if called again
# there are several modes which you can open a file in
# r - read only mode, w - write mode, a - append mode, r+ - read and write mode
