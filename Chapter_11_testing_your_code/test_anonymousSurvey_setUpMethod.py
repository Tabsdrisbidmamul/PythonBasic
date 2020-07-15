import unittest
from survey import AnonymousSurvey


class TestAnonymousSurvey(unittest.TestCase):
	"""Tests for the class AnonymousSurvey"""
	"""
	The setUp() method is a method in the parent class (unittest) so we are 
	essentially overriding it with our own version, but we are doing is 
	creating a storing ground for our instantiated objects so that our test_ 
	methods can access them, and we do not have to re-instantiate them (
	unless we are doing that). 
	
	When we use the setUp() method, python will actually run the setUp() 
	method first, before running any of the test_ methods - so put this at 
	the top!
	
	the attributes that we want are the objects that we want to use - 
	my_survey in this case, so we prepend it with self. so its part of the 
	Test Class and as setUp always runs first, they will be available to use
	
	"""

	def setUp(self):
		"""Create a survey and a set of responses for use in all test
		methods"""
		question = "What language did you first learn to speak?"
		self.my_survey = AnonymousSurvey(question)
		self.responses = ["English", "Spanish", "Mandarin"]

	def test_store_single_response(self):
		"""Test that a single response is stored properly"""
		self.my_survey.store_response(self.responses[0])

		self.assertIn(self.responses[0], self.my_survey.responses)

	def test_store_three_responses(self):
		"""Test that three individual responses are stored properly"""
		for response in self.responses:
			self.my_survey.store_response(response)

		for response in self.responses:
			self.assertIn(response, self.my_survey.responses)
