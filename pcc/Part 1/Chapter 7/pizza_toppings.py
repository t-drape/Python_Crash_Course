message = ""
while message.lower() != 'quit':
	message = input("Topping: ")
	if message.lower() != 'quit':
		print(message.title() + " is a topping for your pizza!")
