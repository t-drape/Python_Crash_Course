class User():

	def __init__(self, first_name, last_name, age, country, birth_month):
		self.first_name = first_name
		self.last_name = last_name
		self.age = age
		self.country = country
		self.birth_month = birth_month

	def describe_user(self):
		print("\nFirst: " + self.first_name + 
			" Last: " + self.last_name + "\nAge: " + self.age +
			"\nBirth Country: " + self.country +
			"\nBirth Month: " + self.birth_month)

	def greet_user(self):
		print("\nHi " + self.first_name + " " + self.last_name + ".")


user = User("T", "D", "15", "US", "Februrary")
user.describe_user()
user.greet_user()

user = User("D", "T", "15", "South Korea", "August")
user.describe_user()
user.greet_user()

user = User("M", "L", "21", "Singapore", "June")
user.describe_user()
user.greet_user()