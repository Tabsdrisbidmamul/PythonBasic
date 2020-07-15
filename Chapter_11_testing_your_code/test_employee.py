import unittest
from employee import Employee


class TestEmployee(unittest.TestCase):
	"""Test the Employee class methods"""

	def setUp(self):
		"""Storing ground for common objects that will be processed by test
		methods"""
		self.employee = Employee("Peter", "File", 50000)

	def test_give_default_raise(self):
		"""Does increasing the employee's annual salary work?"""
		self.employee.give_raise()
		self.assertEqual(self.employee.annual_salary, 55000)

	def test_give_custom_raise(self):
		"""Does increasing the employee's annual salary by a custom amount
		work?"""
		self.employee.annual_salary = 50000
		self.employee.give_raise(10000)
		self.assertEqual(self.employee.annual_salary, 60000)
