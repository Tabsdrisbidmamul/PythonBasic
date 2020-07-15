favourite_number = {
    # dictionary; five names, five numbers
    'sam': 5,
    'Phil': 4,
    'Amy': 19,
    'Bob': 10,
    'Amanda': 20,
}

for key in favourite_number:
    # print each key with its corresponding value
    print(key.title() + ' ' + str(favourite_number[key]))
