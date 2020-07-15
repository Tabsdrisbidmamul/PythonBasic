# make a dictionary with a list of items as the value
favourite_places = {
    'phil': ['town', 'city', 'village', ],
    'dave': ['country-side', 'seaside', 'beach', ],
    'bob': ['town-centre', 'park', 'shopping-centre', ],
}

# iterate through the dictionary and print out the list of values
for name, places in favourite_places.items():
    print('Name: ' + name.title())
    for place in places:
        print('\t\t' + place.title())
