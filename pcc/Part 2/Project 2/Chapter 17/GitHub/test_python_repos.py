import unittest
import requests
import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS

class PythonRepoTestCase(unittest.TestCase):
	"""Tests for 'python_repos.py.'"""

	def test_status_code(self):
		"""Does the API pull return 200?"""
		url = "https://api.github.com/search/repositories?q=language:python&sort=stars"
		r = requests.get(url)
		self.assertEqual(r.status_code, 200)
	def test_length_returned_dictionaries(self):
		"""Does the API pull response dictionary return total count?"""
		url = "https://api.github.com/search/repositories?q=language:python&sort=stars"
		r = requests.get(url)
		response_dict = r.json()
		# Explore information about the repositoreis	
		repo_dicts = response_dict['items']
		count = len(repo_dicts)
		self.assertEqual(count, 30)
	def test_number_repos_total(self):
		"""Does the total count equal 30 or more?"""
		url = "https://api.github.com/search/repositories?q=language:python&sort=stars"
		r = requests.get(url)
		response_dict = r.json()
		# Explore information about the repositoreis	
		count = response_dict['total_count']
		self.assertGreater(count, 29)
	def test_names_Null(self):
		"""Does the name list actually have names stored?"""
		url = "https://api.github.com/search/repositories?q=language:python&sort=stars"
		r = requests.get(url)
		response_dict = r.json()
		# Explore information about the repositoreis
		repo_dicts = response_dict['items']
		names = []
		# Examine the first repository
		for repo_dict in repo_dicts:
			names.append(repo_dict['name'])
		self.assertNotEqual(names, [])

	def test_Chart_Config_data(self):
		"""Was the chart created?"""
		my_style = LS('#333366', base_style=LCS)
		my_style.title_font_size = 24
		my_style.label_font_size = 14
		my_style.major_label_font_size = 18

		my_config = pygal.Config()
		my_config.x_label_rotation = 45
		my_config.show_legend = False
		my_config.truncate_label = 15
		my_config.show_y_guides = False
		my_config.width = 1000

		chart = pygal.Bar(my_config, style=my_style)

		self.assertNotEqual(chart, None)

unittest.main()