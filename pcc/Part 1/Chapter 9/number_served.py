class Restaurant():
	def __init__(self, name, cuisine, number_served=0):
		self.name = name
		self.cuisine = cuisine

	def describe_restaurant(self):
		message = self.name + " is a " + self.cuisine + " restaurant."
		print(message)

	def open_restaurant(self):
		print(self.name + " is now open!")

	def set_number_served(self, number):
		self.number_served = number

	def increment_number_served(self, tables):
		people = tables*5
		self.number_served += people

restaurant = Restaurant('Olive Garden', 'American Italian')
restaurant.describe_restaurant()
restaurant.open_restaurant()
print(restaurant.name)
print(restaurant.cuisine)

restaurant.set_number_served(0)
people = restaurant.number_served
print(people)

restaurant.increment_number_served(tables=10)
people = restaurant.number_served
print(people)