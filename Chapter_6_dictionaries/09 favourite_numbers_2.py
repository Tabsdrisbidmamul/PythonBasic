favourite_number = {
    # dictionary; five names, five numbers
    'sam': [5, 20, 14, ],
    'Phil': [4, 81, 54, ],
    'Amy': [8, 69, 78, ],
    'Bob': [87, 2, 59, ],
    'Amanda': [120, 554, 458, ],
}

# iterate through the dictionary to get the keys and iterate through the
# list of values and print them out too
for name, numbers in favourite_number.items():
    print('Name: ' + name.title())
    for number in numbers:
        print('\tYour favourite number is ' + str(number))
