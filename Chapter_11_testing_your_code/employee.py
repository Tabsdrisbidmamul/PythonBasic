class Employee():
	"""Maps out employee information"""

	def __init__(self, first_name: str, last_name: str, annual_salary: int):
		self.first_name = first_name
		self.last_name = last_name
		self.annual_salary = annual_salary

	def give_raise(self, increase=5000):
		self.annual_salary += increase

