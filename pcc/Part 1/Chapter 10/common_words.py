files = ["summa", "critique of pure reason", "prince"]

for file in files:
	current_file = "Desktop/" + file + ".txt"
	with open(current_file, encoding='utf-8') as f_obj:
		content = f_obj.read()
		print("The book " + "'" + file + "'" + " contains 'the' this many times:")
		content.lower().count("the")
