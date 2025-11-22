from random import randint

class Die():
	"""Models a die with six sides, numbered 1, 6"""
	def __init__(self, sides=6):
		self.sides = sides

	def roll_die(self):
		x = randint(1, self.sides)
		print(x)

d = Die(sides=10)
for i in range(10):
	d.roll_die()

d_20 = Die(sides=20)
for i in range(10):
	d_20.roll_die()