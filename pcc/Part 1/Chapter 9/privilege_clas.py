from user_class import User

class Admin(User):

	def __init__(self, first_name, last_name, age, country, birth_month):

		super().__init__(first_name, last_name, age, country, birth_month)

		self.privileges = ["can add post", "can ban user from commenting", "can remove threads"]

	def show_privileges(self):
		for privilege in self.privileges:
			print(privilege)