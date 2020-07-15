# a program that asks the user how many are dining tonight
message = 'How many are dining today? '
# convert the inputted numerical value into a integer
dining_group = abs(int(input(message)))

# a statement to see if the amount wanting to dine is more than 8,
# then print said message, otherwise print this message
if dining_group > 8:
    print('You\'ll have to wait for a table')
else:
    print('there is a table available to dine at')
