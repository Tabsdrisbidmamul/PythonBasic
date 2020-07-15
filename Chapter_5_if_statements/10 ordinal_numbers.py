ordinal_numbers = list(range(1, 11))   # make a list of number from 1 to 10

for number in ordinal_numbers:   # loop through the list
    if number == 1:
        print(str(number) + 'st')   # add st to 1
    elif number == 2:
        print(str(number) + 'nd')   # add nd to 2
    elif number == 3:
        print(str(number) + 'rd')   # add rd to 3
    else:
        print(str(number) + 'th')   # add th to the rest
