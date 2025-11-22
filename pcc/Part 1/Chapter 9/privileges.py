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

class Admin(User):
	def __init__(self, first_name, last_name, age, country, birth_month):

		super().__init__(first_name, last_name, age, country, birth_month)

		self.privileges = Privileges()

class Privileges():

	def __init__(self, privileges=["can add new rules", "can ban users from commenting", "can remove old posts"]):
		self.privileges = privileges

	def show_privileges(self):
		for privilege in self.privileges:
			print(privilege)

new_admin = Admin("Edna", "Wart", 74, "US", "January")

new_admin.privileges.show_privileges()