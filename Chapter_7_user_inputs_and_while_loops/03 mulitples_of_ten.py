# ask the user to input a number
message = 'Enter a number: '

# convert the inputted number into a integer
multiple_of_ten = abs(int(input(message)))

# if the inputted number is divided by 10 and if the remainder is 0,
# then the number is a multiple of ten, if there is a remainder, then it isn't
if multiple_of_ten % 10 == 0:
    print('this number is a multiple of ten')
else:
    print('this number is not a multiple of ten')
