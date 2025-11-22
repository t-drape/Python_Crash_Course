class Employee():
	"""Collect data on employees"""

	def __init__(self, first_name, last_name, annual_salary):
		self.first_name = first_name
		self.last_name = last_name
		self.annual_salary = int(annual_salary)

	def give_raise(self, bonus=5000):
		"""Add money to employees annual salary"""
		self.annual_salary += int(bonus)
