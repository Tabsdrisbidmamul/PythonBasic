# a program that will aks why you like programming
filename = 'programming_poll.txt'

while True:
	user_input = str(input('Why do you like programming? '))
	with open(filename, 'a') as file_object:
		file_object.write('\n' + user_input + '\n')

# essentially the program is just like the previous example
