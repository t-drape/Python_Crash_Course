def print_models(unprinted_designs, completed_models):
	"""Takes a list and simulates the process of printing, transferring 
	from one list to another the printed designs"""

	while unprinted_designs:
		current_design = unprinted_designs.pop()

		print("Printing model: " + current_design)
		completed_models.append(current_design)


def show_completed_models(completed_models):
	"""Takes a list and prints all items in it"""
	
	print("\nThe following models have been printed: ")
	for completed_model in completed_models:
		print(completed_model)