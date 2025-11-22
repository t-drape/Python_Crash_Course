number = input("What is your number? ")
mod = int(number) % 10 

if mod > 0:
	print(number + " is not a multiple of ten.")
else:
	print(number + " is a multiple of ten.")