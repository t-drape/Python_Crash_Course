import json
# Retrieve current favorite number, or get a new favorite number

filename = "Desktop/number.json"

try:
	with open(filename) as f_obj:
		number = json.load(f_obj)
		print("I know your favorite number! It's " + number + ".")

except FileNotFoundError:
	number = input("What is your favorite number? ")

	filename = "Desktop/number.json"

	with open(filename, 'w') as f_obj:
		json.dump(number, f_obj)