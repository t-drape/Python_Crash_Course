import unittest
from employee import Employee

class TestEmployee(unittest.TestCase):
	"""Tests for the class Employee"""

	def setUp(self):

		self.employee = Employee("T", "D", "5000")

	def test_give_default_raise(self):
		self.employee.give_raise()

	def test_give_custom_raise(self):
		self.employee.give_raise(bonus=10000)

unittest.main()