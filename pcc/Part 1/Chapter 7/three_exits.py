while True:
	age = input("What is your age? ")
	if age != "quit":
		age = int(age)
		if age < 3:
			print("Your ticket is free!")
		elif age > 2 and age < 13:
			print("Your ticket is $10!") 
		elif age > 12:
			print("Your ticket is $15!")
	else: 
		break