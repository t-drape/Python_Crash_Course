"""Data courtesy The World Bank,
 url: https://data.worldbank.org/indicator/SP.DYN.LE00.IN.
 accessed through Kaggle,
 url: https://www.kaggle.com/datasets/gemartin/world-bank-data-1960-to-2016"""
import csv

import pygal
from pygal.style import RotateStyle as RS, NeonStyle as NS

from country_code import get_country_code

file = './fertility_rate.csv'

with open(file) as f:
	reader = csv.reader(f)
	header_row = next(reader)

	# cc_fr
	cc_fr = {}
	i = 0
	for row in reader:
		try:
			country_name = row[0]
			fertility_rate = row[65]
			try:
				fertility_rate = float(fertility_rate)
				code = get_country_code(country_name)
				if code:
					cc_fr[code] = fertility_rate
			except ValueError:
				continue
		except IndexError:
			continue

cc_1, cc_2, cc_3 = {}, {}, {}
for cc, fr in cc_fr.items():
	if fr < float(1.5):
		cc_1[cc] = fr
	elif fr < float(3.5):
		cc_2[cc] = fr
	else:
		cc_3[cc] = fr


wm_style = RS('#996633', base_style=NS)
wm = pygal.maps.world.World(style=wm_style)
wm.title = "Fertility by Country - 2021"
wm.add("0-1.5 babies per woman", cc_1)
wm.add("1.5-3.5 babies per woman", cc_2)
wm.add(">3.5 babies per woman", cc_3)
wm.precision = 3

wm.render_to_file("./rate.svg")
			