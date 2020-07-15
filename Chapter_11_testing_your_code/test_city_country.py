"""
Run tests to see if they fall within range, by using the 6 methods described in
test_name_function.py
"""

from unittest import TestCase
from city_functions import city_country


class TestCity_country(TestCase):
	def test_city_country(self):
		"""Do city's such as 'Santiago, Chile' work?"""
		formatted_cities = city_country('santiago', 'chile')
		self.assertEqual(formatted_cities, 'Santiago, Chile')

	def test_city_country_population(self):
		"""Adding population to a city, country - 'Santiago, Chile -
		Population xxx' work?"""
		formatted_cities = city_country('santiago', 'chile', population=500000)
		self.assertEqual(formatted_cities, 'Santiago, Chile - Population 500000')
