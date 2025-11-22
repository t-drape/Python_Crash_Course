cities = {
	"tokyo": {
		"country": "japan",
		"population": "13.96 million",
		"fact": "ultra-modern and traditional",
		},
	"shanghai": {
		"country": "china",
		"population": "26.32 million",
		"fact": "china's financial hub",
		},
	"washington, d.c.": {
		"country": "usa",
		"population": "712,816",
		"fact": "compact city",
		}
	}
for city, city_info in cities.items():
	print("\n" + city.title())
	for key, value in city_info.items():
		print("\n\t" + key.title() + ": " + value.title())
