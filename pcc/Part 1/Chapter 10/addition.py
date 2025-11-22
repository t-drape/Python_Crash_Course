number_1 = input("First number: ")
number_2 = input("Second number: ")

try:
	number = int(number_1) + int(number_2)
	print(number)
except ValueError:
	print("You can't numbers and text!")