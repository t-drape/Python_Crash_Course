def city_and_country(city, country, population=""):
	if population:
		msg = city + ", " + country + " - population " + population
	else:
		msg = city + ", " + country
	return msg