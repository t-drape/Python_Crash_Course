import json

import pygal
from pygal.style import RotateStyle as RS, DarkStyle as DS

from country_code import get_country_code

file = "Desktop/global_gdp.json"

with open(file) as f:
	pop_data = json.load(f)

# Print the GDP of each country in 2014
cc_populations = {}
for pop_dict in pop_data:
	if pop_dict['Year'] == '2014':
		country_name = pop_dict['Country Name']
		gdp = float(pop_dict['Value'])
		code = get_country_code(country_name)
		if code:
			cc_populations[code] = gdp

gdp_1, gdp_2, gdp_3 = {}, {}, {}

for cc, gdp in cc_populations.items():
	if gdp < 1000000000000:
		gdp_1[cc] = gdp
	elif gdp < 10000000000000:
		gdp_2[cc] = gdp
	else:
		gdp_3[cc] = gdp


wm_style = RS('#996633', base_style=DS)
wm = pygal.maps.world.World(style=wm_style)
wm.title = "GDP of each country - 2014"
wm.add("0-1tr", gdp_1)
wm.add("1tr-10tr", gdp_2)
wm.add(">1tr", gdp_3)

wm.render_to_file("Desktop/gdp.svg")