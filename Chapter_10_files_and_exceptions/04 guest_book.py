# program that asks the user name, once entered print a prompt to say it was
# accepted and append the string onto the file

filename = 'programming.txt'

while True:
	userName = str(input('What is your name? '))
	print('Welcome ', userName)
	with open(filename, 'a') as file_object:
		# the \n is required, as the write method doesn't put newlines,
		# so it has to be put in manually
		file_object.write('\n' + userName + ' has been recorded\n')
