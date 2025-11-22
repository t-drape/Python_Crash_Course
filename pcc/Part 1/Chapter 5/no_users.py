usernames = []

if usernames:
	for name in usernames:
		if name == "admin":
			print("Hello " + name + " would you like to see a status report?")
		else:
			print("Hello " + name + "thank you for logging in!")
else:
	print("We need some users!")