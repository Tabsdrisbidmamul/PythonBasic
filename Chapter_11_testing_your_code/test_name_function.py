"""
When writing unittest(s) the file name must always start with 'test' - or
the unittest module won't be able to build the testing environment.

We import unittest (for its TestCase class, we write all of our tests that
we want to do within a class, so that it can inherit the methodology and
attributes of that class.

we also import our functions a script or classes into the file as well

When writing the tests, we write them within methods that must always start
with 'test' and always make sure that they are descriptive so when it comes
to doing the test, we can se method test_first_last_name: True is a lot more
helpful in the long run

We write statements to get a functions return value and we can use 6
different methods to see whether or not the value fits within range

all the methods have self. prepended on them

assertEqual(a, b) -> a==b
assertNotEqual(a, b) -> a!=b
assertTrue(x) -> is x True?
assertFalse(x) -> is x False?
assertIn(item, list) -> is the item in the list (can be other than list)
assertNotIn(item, list) -> is the item not in the list
"""

import unittest
from name_function import get_formatted_name


class NamesTestCase(unittest.TestCase):
	"""Tests for 'name_function.py'"""

	def test_first_last_name(self):
		"""Do names like 'Janis Joplin' work?"""
		formatted_name = get_formatted_name('janis', 'joplin')
		self.assertEqual(formatted_name, 'Janis Joplin')

	def test_first_last_middle_name(self):
		"""Do names like 'Wolfgang Amadeus Mozart' work?"""
		formatted_name = get_formatted_name('wolfgang', 'Mozart', 'Amadeus')
		self.assertEqual(formatted_name, 'Wolfgang Amadeus Mozart')

# add this to run the mainloop unittest from cmd line
#unittest.main()
