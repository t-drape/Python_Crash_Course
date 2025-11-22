import unittest
from country_code import get_country_code

class CountryTestCase(unittest.TestCase):
	"""Tests for 'country_code.py.'"""

	def test_get_country_code(self):
		"""Do countries like 'Yemen' return correct code ('ye')?"""
		cc = get_country_code("Yemen")
		self.assertEqual(cc, 'ye')

unittest.main()