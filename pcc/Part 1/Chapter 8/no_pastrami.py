sandwiches_order = ["pastrami", "ham", "cheese", "pastrami", "salami", "pastrami", "open-faced"]
finished_orders = []
print("Our deli has run out of pastrami, sorry for the inconvenience.")
while "pastrami" in sandwiches_order:
	sandwiches_order.remove("pastrami")
while sandwiches_order:
	new_sandwich = sandwiches_order.pop()
	print("Your " + new_sandwich + " sandwich is ready!")
	finished_orders.append(new_sandwich)

print(finished_orders)