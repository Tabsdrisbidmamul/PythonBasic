person_0 = {
    # dictionary containing information about a person
    'first_name': 'Phil',
    'last_name': 'Still',
    'age': 21,
    'city': 'New York',
}

person_1 = {
    # dictionary containing information about a person
    'first_name': 'bob',
    'last_name': 'reeves',
    'age': 32,
    'city': 'Texas',
}

person_2 = {
    # dictionary containing information about a person
    'first_name': 'steve',
    'last_name': 'rogers',
    'age': 18,
    'city': 'California',
}

# make a list containing all dictionaries
people = [person_0, person_1, person_2]

# loop through the list
for person in people:
    print(person)
