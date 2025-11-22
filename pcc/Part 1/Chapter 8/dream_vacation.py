responses = {}


polling_active = True


while polling_active: 

	name = input("What is your name?\n ")
	vacation_spot = input("In your dreams, where would you like to go?\n")


	responses[name] = vacation_spot

	next_person = input("Would you like another person to poll? (y/n) ")

	if next_person.lower() == "n":
		polling_active = False

print("Poll Results")
for name, response in responses.items():
	print(name.title() + " wants to go to " + response.title() + ".")