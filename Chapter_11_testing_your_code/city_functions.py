"""
Simple function to neatly format the city, country and population
"""

def city_country(city, country, population=None):
	if population:
		formatted_city = "{0}, {1} - Population {2}".format(city, country,
												 str(population))
	else:
		formatted_city = "{0}, {1}".format(city, country)
	return formatted_city.title()

