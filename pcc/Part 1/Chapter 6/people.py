person_1 = {"name_f": "Lia", "name_l": "Dr", "age": "21", "city": "Phoenix"}
person_2 = {"name_f": "TJ", "name_l": "Dr", "age": "15", "city": "Tokyo"}
person_3 = {"name_f": "Ot", "name_l": "Mel", "age": "28", "city": "Beijing"}

people = [person_1, person_2, person_3]

for person in people:
	for key, value in person.items():
		print(key + ":")
		print(value + "\n")