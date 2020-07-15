# program to test try-except and else block
import time


def addition():
	"""Asks to add two number together"""
	print('Enter two numbers and I\'ll them together')
	while True:
		f_num = input('\nEnter the first number please: ')
		s_num = input('Enter the second number please: ')

		# When you think an error may occur, place it within the try block
		# the try block is always followed by a an except block where the
		# error in question can be raised, for example:
		# ZeroDivisionError, FileNotFoundError, ValueError and many more
		try:
			answer = int(f_num) + int(s_num)
		# the error in question is raised and you can put messages here to
		# say 'error was occurred because of x thing here'
		# it can be as simple as a message saying that or a whole extract of
		# code of what to do in an event like that
		# sometimes you may want it to 'fail silently' in which you can
		# write 'pass' within the clause and it acts as a placeholder,
		# python will run it, but it doesn't return anything, its a
		# placeholder indicating that you either want it filled or to fail
		# silently
		except ValueError:
			print("\nSorry, enter number's please")
			time.sleep(0.5)
		# the else clause is here so the program will keep running if the
		# except clause failed, if the else clause was not here, the program
		# will either stop at the except clause - if the code there tells
		# it to do - or carry on depending on the code, but usually it will
		# end at the except clause

		# the else clause will run when true and is usually the part of the
		# code that was initially meant to be ran at the try block is placed
		else:
			print('\n' + str(answer))


addition()
# the try-except-else block can prevent crashes in your program, prevent the
# traceback being called and being showed to the user - this can prevent
# malicious attacks or just not show the user freight-full code to the user
