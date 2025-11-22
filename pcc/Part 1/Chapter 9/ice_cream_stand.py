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

class IceCreamStand(Restaurant):
	def __init__(self, name, cuisine, number_served=0):
		super().__init__(name, cuisine, number_served)
		self.flavors = ["Vanilla", "Chocolate"]

	def show_flavors(self):
		for flavor in self.flavors:
			print(flavor)

icr = IceCreamStand("Stand", "Dessert")
icr.flavors.append("Strawberry")
icr.show_flavors()