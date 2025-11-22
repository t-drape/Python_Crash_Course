import json

number = input("What is your favorite number? ")

filename = "Desktop/number.json"

with open(filename, 'w') as f_obj:
	json.dump(number, f_obj)