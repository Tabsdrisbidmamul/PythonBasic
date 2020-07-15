# make a function that has 2 parameters
def describe_city(city, country='England'):
    """A function that will return the city and country in a sentence"""
    print('\n' + city.title() + ' is in ' + country.title())

# call one of the function with the default parameter
describe_city(city='London')
describe_city(city='Rome', country='Italy')
describe_city(city='Paris', country='France')