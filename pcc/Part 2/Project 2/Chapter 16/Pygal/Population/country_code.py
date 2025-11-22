from pygal_maps_world.i18n import COUNTRIES

def get_country_code(country):
	""""Return the pygal two-digit country code for given country."""
	for code, name in COUNTRIES.items():
		if name == country:
			return code
		# Get countries in South America
		elif country == 'Venezuela, RB':
			return 've'
		elif country == 'Yemen, Rep.':
			return 'ye'
		elif country == 'Bolivia':
			return 'bo'
		# Get the countries in Africa
		elif country == 'Egypt, Arab Rep.':
			return 'eg'
		elif country == 'Libya':
			return 'ly'
		elif country == 'Congo, Dem. Rep.':
			return 'cd'
		elif country == 'Congo, Rep.':
			return 'cg'
		elif country == 'Tanzania':
			return 'tz'


		# Get Asian Countries
		elif country == 'Korea, Dem. Rep.':
			return 'kp'
		elif country == 'Korea, Rep.':
			return 'kr'
		elif country == 'Iran, Islamic Rep.':
			return 'ir'
		elif country == 'Vietnam':
			return 'vn'

	# If country not found return none
	return None