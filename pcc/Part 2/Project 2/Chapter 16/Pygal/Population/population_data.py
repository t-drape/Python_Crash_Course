import json

import pygal
from pygal.style import RotateStyle as RS, LightColorizedStyle as LCS, DarkStyle as DS

from country_code import get_country_code

file = "./population_data.json"

with open(file) as f:
	pop_data = json.load(f)

# Print the 2010 population for each country
cc_populations = {}
for pop_dict in pop_data:
	if pop_dict['Year'] == '2010':
		country_name = pop_dict["Country Name"]
		population = int(float(pop_dict["Value"]))
		code = get_country_code(country_name)
		if code:
			cc_populations[code] = population
# Group the countries into 3 population levels.
cc_1, cc_2, cc_3 = {}, {}, {}
for cc, pop in cc_populations.items():
	if pop < 10000000:
		cc_1[cc] = pop
	elif pop < 1000000000:
		cc_2[cc] = pop
	else:
		cc_3[cc] = pop

wm_style = RS('#336699')
wm = pygal.maps.world.World(style=wm_style)
wm.title = "World Population in 2010, by Country"
wm.add('0-10m', cc_1)
wm.add('10m-1bn', cc_2)
wm.add('>1bn', cc_3)

wm.render_to_file("./wp.svg")