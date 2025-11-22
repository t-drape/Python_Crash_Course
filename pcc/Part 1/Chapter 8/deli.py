sandwiches_order = ["ham", "cheese", "pastrami", "salami", "open-faced"]
finished_orders = []
while sandwiches_order:
	new_sandwich = sandwiches_order.pop()
	print("Your " + new_sandwich + " sandwich is ready!")
	finished_orders.append(new_sandwich)

print(finished_orders)