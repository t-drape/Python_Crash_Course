files = ["cats.txt", "dogs.txt"]
for file in files:
	file_path = "Desktop/" + file
	try:
		with open(file_path) as f_obj:
			names = f_obj.readlines()
		for name in names:
			breed = name.title()
			print(breed.strip())
	except FileNotFoundError:
		print("I could not find the file " + "'" + file + "'")