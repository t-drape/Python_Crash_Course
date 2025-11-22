with open("desktop/guest.txt", 'w') as f_obj:
	name = input("What is your name? ")
	f_obj.write(name)