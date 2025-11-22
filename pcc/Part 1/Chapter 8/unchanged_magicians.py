def make_great(magicians, great_magicians):
	"""Takes a list of magicians and makes them 'The Great ...'"""
	
	while magicians:
		mago = magicians.pop()
		mago = "The great " + mago
		mago = mago.title()
		great_magicians.append(mago)
	return magicians


def show_magicians(magicians):
	"""Prints every magician from a list and prints there name"""

	for magician in magicians:
		print(magician.title())

magicians = ["Houdini", "david blaine", "shin lim"]
great_magicians = []


new_magicians = make_great(magicians[:], great_magicians)

show_magicians(magicians)

show_magicians(great_magicians)

show_magicians(new_magicians)