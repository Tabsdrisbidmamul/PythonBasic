# make the function with city and country
def city_country(city, country):
    """A function that will return the city and country"""
    full_city = city + ', ' + country
    # return the value as this variable
    return full_city.title()

# store the function call into a variable for the return value to work,
# then print it off


place_0 = city_country(city='London', country='England')
print(place_0)
place_1 = city_country('Rome', 'Italy')
print(place_1)
place_2 = city_country(country='France', city='paris')
print(place_2)
