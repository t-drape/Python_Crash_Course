class Restaurant():
	def __init__(self, name, cuisine):
		self.name = name
		self.cuisine = cuisine

	def describe_restaurant(self):
		message = self.name + " is a " + self.cuisine + " restaurant."
		print(message)

	def open_restaurant(self):
		print(self.name + " is now open!")

restaurant = Restaurant('Olive Garden', 'American Italian')
restaurant.describe_restaurant()
restaurant.open_restaurant()
print(restaurant.name)
print(restaurant.cuisine)