while True:
	number_1 = input("First number: ")
	if number_1 == 'q':
		break
	number_2 = input("Second number: ")
	if number_2 == 'q':
		break
	try:
		number = int(number_1) + int(number_2)
		print(str(number) + "\n")
	except ValueError:
		print("You can't numbers and text!\n")