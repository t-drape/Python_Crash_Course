import unittest
from city_functions import city_and_country

class NameTestCase(unittest.TestCase):
	"""Test city_and_country.py"""

	def test_city_and_country(self):
		"""Do cities like 'Santiago, Chile' work?"""
		msg = city_and_country("Santiago", "Chile")
		self.assertEqual(msg, "Santiago, Chile")

	def test_city_country_population(self):
		msg = city_and_country("Santiago", "Chile", "5000000")
unittest.main()