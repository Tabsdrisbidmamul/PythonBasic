# make a dictionary of cities, and have the values as a nested dictionary
# with the country, population and facts
cities = {
    'london': {
        'country': 'England',
        'population': 8.788 * (10 ** 6),
        'fact': 'London bridge fell down',
    },
    'Tokyo': {
        'country': 'Japan',
        'population': 9.273 * (10 ** 6),
        'fact': 'Anime comes from this place',
    },
    'Rome': {
        'country': 'Italy',
        'population': 2.868 * (10 ** 6),
        'fact': 'The colosseum is here',
    },
}

# the variable city is for the keys (london, tokyo, rome) and city_info is
# another variable for  the keys (country, population and fact
for city, city_info in cities.items():
    print('\nCity: ' + city.title())
    location = city_info['country']

    print('\tLocation: ' + location.title())
    print('\tPopulation: ' + str(city_info['population']))
    print('\tFact: ' + city_info['fact'])

