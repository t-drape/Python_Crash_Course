rivers = {"amazon": "brazil", "missisipi": "USA", "yellow": "china"}

for river, country in rivers.items():
	if country.lower() == "usa":
		print("The " + river.title() + " river runs through " + country.upper() + ".")
	else:
		print("The " + river.title() + " river runs through " + country.title() + ".")

for river in rivers:
	print(river)

for country in rivers.values():
	print(country)