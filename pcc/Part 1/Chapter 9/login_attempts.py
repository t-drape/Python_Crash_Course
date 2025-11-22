class User():

	def __init__(self, first_name, last_name, age, country, birth_month, login_attempt=0):
		self.first_name = first_name
		self.last_name = last_name
		self.age = age
		self.country = country
		self.birth_month = birth_month
		self.login_attempt = login_attempt

	def describe_user(self):
		print("\nFirst: " + self.first_name + 
			" Last: " + self.last_name + "\nAge: " + self.age +
			"\nBirth Country: " + self.country +
			"\nBirth Month: " + self.birth_month)

	def greet_user(self):
		print("\nHi " + self.first_name + " " + self.last_name + ".")

	def increment_login_attempts(self):
		self.login_attempt += 1

	def reset_login_attempts(self):
		self.login_attempt = 0


user = User("T", "D", "15", "US", "Februrary")
user.describe_user()
user.greet_user()

user = User("D", "T", "15", "South Korea", "August")
user.describe_user()
user.greet_user()

user = User("M", "L", "21", "Singapore", "June")
user.describe_user()
user.greet_user()

user.increment_login_attempts()
user.increment_login_attempts()
user.increment_login_attempts()
user.increment_login_attempts()
print(user.login_attempt)
user.reset_login_attempts()
print(user.login_attempt)
user.increment_login_attempts()
user.increment_login_attempts()
user.increment_login_attempts()
user.increment_login_attempts()
print(user.login_attempt)
user.reset_login_attempts()
print(user.login_attempt)