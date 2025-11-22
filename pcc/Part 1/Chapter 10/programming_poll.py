filename = "Desktop/programming_poll.txt"

with open(filename, 'a') as file:
	print("Press 'q' to quit.")
	while True:
		reason = input("Why do you like programming? ")
		if reason == 'q':
			break
		file.write(reason.strip() + "\n")
		