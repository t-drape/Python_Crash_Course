filename = 'Desktop/guest_book.txt'

with open(filename, 'w') as file:
	while True:
		print("\nPress 'q' to quit." )
		guest = input("What is your name? ")
		if guest == 'q':
			break
		file.write(guest + "\n")