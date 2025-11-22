def car_info(make, model, **features):
	"""Takes a variable of the make of a car and its model, as well as any 
	features, and returns a dictionary to the user"""

	car = {}
	car["make"] = make
	car["model"] = model

	for key, value in features.items():
		car[key] = value
	return car

car = car_info("Lamborghini", "Urus Peformante", engine="V8", horsepower="657")
