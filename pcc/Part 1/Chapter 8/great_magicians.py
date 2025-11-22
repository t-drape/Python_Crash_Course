def make_great(magicians, great_magicians):
	while magicians:
		mago = magicians.pop()
		mago = "The great " + mago
		mago = mago.title()
		great_magicians.append(mago)

	
def show_magicians(magicians):
	for magician in magicians:
		print(magician.title())

magicians = ["Houdini", "david blaine", "shin lim"]
great_magicians = []

show_magicians(magicians)

make_great(magicians, great_magicians)

show_magicians(great_magicians)