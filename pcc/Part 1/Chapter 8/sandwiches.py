def sandwich_order(size, *toppings):
	print("Thank you for your order of a "
	 + str(size) + "-in. sub with these toppings:")
	for topping in toppings:
		print("- " + topping)

sandwich_order(6, "cheese", "basil", "tomatoes")

sandwich_order(12, "chili")

sandwich_order(8, "onion", "pepper", "pepperoni", "ranch")
